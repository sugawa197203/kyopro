using System;
using System.Collections;
using System.Diagnostics.CodeAnalysis;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Runtime.Intrinsics;
using System.Text;

public static class Program
{
	public static void Main()
	{
		var (N, K, H, T, D) = InputUtil.ReadLine<uint>();
		Color[] targetColors = new Color[H];
		Color[] ownColorSet = new Color[K];

		for (int i = 0; i < K; i++)
		{
			var (r, g, b) = InputUtil.ReadLine<double>();
			ownColorSet[i] = new Color(r, g, b);
		}

		Palette palette = new((int)N, ownColorSet);


		for (int i = 0; i < H; i++)
		{
			var (r, g, b) = InputUtil.ReadLine<double>();
			targetColors[i] = new Color(r, g, b);
		}

		// 初期状態
		Console.Write(palette.ToString());
		double diffsum = 0;

		// とりあえず近い色出す
		foreach (var targetColor in targetColors)
		{
			var exits = palette.GetNirestColorByExistingColors(targetColor);
			double diffExists = exits.Item1 == null ? double.MaxValue : targetColor.SumDiff((Color)exits.Item1);

			var own = palette.GetNirestColorByOwnColor(targetColor);
			double diffOwn = targetColor.SumDiff(own.GetColor());

			var createable = palette.GetNirestColorByCreateable(targetColor);
			double diffCreateable = targetColor.SumDiff(createable.GetColor());

			// Console.Error.WriteLine($"duff: {diffExists} {diffOwn} {diffCreateable}");

			if (!(exits.Item2 == null))
			{
				if (diffExists <= diffOwn && diffExists <= diffCreateable)
				{
					// Console.Error.WriteLine($"exitsColor");
					Vec2 position = (Vec2)exits.Item2;
					palette.PickColor(position.X, position.Y);
					Console.WriteLine($"2 {position.X} {position.Y}");
					continue;
				}
			}
			if (diffOwn < diffExists && diffOwn < diffCreateable)
			{
				// Console.Error.WriteLine($"ownColor");
				if (palette.TryGetFreePosition(out Vec2 position))
				{
					palette.PlaceColor(position.X, position.Y, own.GetColor());
					Console.WriteLine($"1 {position.X} {position.Y} {own.K}");
					palette.PickColor(position.X, position.Y);
					Console.WriteLine($"2 {position.X} {position.Y}");
					continue;
				}
			}
			else
			{
				// Console.Error.WriteLine($"createableColor");
				switch (createable)
				{
					case Mix mix when mix.Recipe2 is Direct _direct:
						// Console.Error.WriteLine($"Direct + Direct");
						if (palette.TryGetFreePosition(out Vec2 position))
						{
							Direct d1 = (Direct)mix.Recipe1;
							palette.PlaceColor(position.X, position.Y, d1.GetColor());
							palette.PlaceColor(position.X, position.Y, _direct.GetColor());
							Console.WriteLine($"1 {position.X} {position.Y} {d1.K}");
							Console.WriteLine($"1 {position.X} {position.Y} {_direct.K}");
							palette.PickColor(position.X, position.Y);
							Console.WriteLine($"2 {position.X} {position.Y}");
						}
						break;
					case Mix mix when mix.Recipe2 is Exits exit:
						// Console.Error.WriteLine($"Exits + Direct");
						Direct direct = (Direct)mix.Recipe1;
						palette.PlaceColor(exit.Position.X, exit.Position.Y, direct.GetColor());
						Console.WriteLine($"1 {exit.Position.X} {exit.Position.Y} {direct.K}");
						palette.PickColor(exit.Position.X, exit.Position.Y);
						Console.WriteLine($"2 {exit.Position.X} {exit.Position.Y}");

						break;
				}
				continue;
			}

			palette.PickColor(exits.Item2.Value.X, exits.Item2.Value.Y);
			Console.WriteLine($"2 {exits.Item2.Value.X} {exits.Item2.Value.Y}");
		}

		// Console.Error.WriteLine($"Initial diff sum: {diffsum}");
	}

}

public struct Vec2 : IEquatable<Vec2>, IEqualityComparer<Vec2>
{
	public int X { get; }
	public int Y { get; }

	public Vec2(int x, int y)
	{
		X = x;
		Y = y;
	}

	public static Vec2 operator +(Vec2 a, Vec2 b)
	{
		return new Vec2(a.X + b.X, a.Y + b.Y);
	}

	public static Vec2 operator -(Vec2 a, Vec2 b)
	{
		return new Vec2(a.X - b.X, a.Y - b.Y);
	}

	public static bool operator ==(Vec2 a, Vec2 b)
	{
		return a.Equals(b);
	}

	public static bool operator !=(Vec2 a, Vec2 b)
	{
		return !a.Equals(b);
	}

	public readonly bool Equals(Vec2 other)
	{
		return X == other.X && Y == other.Y;
	}

	public readonly bool Equals(Vec2 x, Vec2 y)
	{
		return x.Equals(y);
	}

	public readonly int GetHashCode([DisallowNull] Vec2 obj)
	{
		return obj.X.GetHashCode() ^ obj.Y.GetHashCode();
	}

	public override bool Equals(object obj)
	{
		return obj is Vec2 && Equals((Vec2)obj);
	}

	public override int GetHashCode()
	{
		throw new NotImplementedException();
	}
}

public interface IRecipe
{
	public Color GetColor();
}

public class Direct : IRecipe
{
	public int K;
	private Color C;
	public Direct(int k, Color c)
	{
		this.K = k;
		C = c;
	}

	public Color GetColor()
	{
		return C;
	}
}

public class Exits : IRecipe
{
	public Vec2 Position { get; }
	private Color C;
	public Exits(Vec2 position, Color c)
	{
		Position = position;
		C = c;
	}

	public Color GetColor()
	{
		return C;
	}
}

public class Mix : IRecipe
{
	public IRecipe Recipe1 { get; }
	public IRecipe Recipe2 { get; }
	private Color C;
	public Mix(IRecipe recipe1, IRecipe recipe2, Color c)
	{
		Recipe1 = recipe1;
		Recipe2 = recipe2;
		C = c;
	}

	public Color GetColor()
	{
		return C;
	}
}

public class Palette
{
	public Color[,] Grid { get; }
	public bool[,] horizontalWall { get; }
	public bool[,] verticalWall { get; }
	private int N;
	private Color[] ownColors;
	private Dictionary<Color, int> ownColorToRecipe = new();
	public Palette(int n, Color[] own)
	{
		N = n;
		Grid = new Color[n, n];
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				Grid[i, j] = Color.None; // 初期化
			}
		}

		verticalWall = new bool[n, n - 1];
		horizontalWall = new bool[n - 1, n];

		for (int i = 0; i < n; i++)
		{
			for (int j = 1; j < n - 1; j += 2)
			{
				verticalWall[i, j] = true;
			}
		}

		for (int i = 0; i < n - 1; i++)
		{
			for (int j = 0; j < n; j++)
			{
				horizontalWall[i, j] = true;
			}
		}

		ownColors = own;
		for (int i = 0; i < own.Length; i++)
		{
			ownColorToRecipe[own[i]] = i;
		}
	}

	public bool TryGetFreePosition(out Vec2 position)
	{
		// for (int i = 0; i < N; i++)
		// {
		// 	for (int j = 0; j < N; j += 2)
		// 	{
		// 		Console.Error.Write($"{Grid[i, j] == Color.None} ");
		// 	}
		// 	Console.Error.WriteLine();
		// }

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j += 2)
			{
				if (Grid[i, j] == Color.None)
				{
					position = new Vec2(i, j);
					// Console.Error.WriteLine($"Free position found at ({i}, {j})");
					// Console.ReadLine();
					return true;
				}
			}
		}
		position = default;
		// Console.ReadLine();
		return false;
	}

	public void PlaceColor(int x, int y, Color color)
	{
		if (x < 0 || x >= N || y < 0 || y >= N)
		{
			throw new ArgumentOutOfRangeException("Position is out of bounds.");
		}

		Grid[x, y] = Grid[x, y].Marge(color);
	}

	public void PickColor(int x, int y)
	{
		if (x < 0 || x >= N || y < 0 || y >= N)
		{
			throw new ArgumentOutOfRangeException("Position is out of bounds.");
		}

		Grid[x, y].Sub(1);
	}

	public List<(Color, Mix)> GetCreatableColors()
	{
		var creatableColors = ownColors
						.SelectMany(_ => ownColors, (c1, c2) => (c1.Marge(c2), new Mix(new Direct(ownColorToRecipe[c1], c1), new Direct(ownColorToRecipe[c2], c2), c1.Marge(c2))))
						.ToList();
		return creatableColors;
	}
	public List<(Color, Mix)> GetCreatableColorsByExist()
	{
		var exitsColors = new List<(Color, Exits)>();
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j += 2)
			{
				if (Grid[i, j] != Color.None)
				{
					exitsColors.Add((Grid[i, j], new Exits(new Vec2(i, j), Grid[i, j])));
				}
			}
		}
		var creatableColors = ownColors
						.SelectMany(_ => exitsColors, (c1, c2) => (c1.Marge(c2.Item1), new Mix(new Direct(ownColorToRecipe[c1], c1), c2.Item2, c1.Marge(c2.Item1))))
						.ToList();
		return creatableColors;
	}

	public (Color, IRecipe) GetNirest(Color targetColor, List<(Color, IRecipe)> list)
	{
		double minDiff = double.MaxValue;
		Color? bestColor = null;
		IRecipe? bestRecipe = null;

		foreach (var (color, recipe) in list)
		{
			double diff = targetColor.SumDiff(color);
			if (diff < minDiff)
			{
				minDiff = diff;
				bestColor = color;
				bestRecipe = recipe;
			}
		}

		if (bestColor == null || bestRecipe == null)
		{
			throw new InvalidOperationException("No suitable color found.");
		}

		return ((Color)bestColor, bestRecipe);
	}

	public (Color?, Vec2?) GetNirestColorByExistingColors(Color targetColor)
	{
		double diff = double.MaxValue;
		Vec2? closestPosition = null;
		Color? closestColor = null;

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j += 2)
			{
				Color currentColor = Grid[i, j];
				if (currentColor == Color.None) continue;
				double currentDiff = targetColor.SumDiff(currentColor);
				if (currentDiff < diff)
				{
					diff = currentDiff;
					closestPosition = new Vec2(i, j);
					closestColor = currentColor;
				}
			}
		}
		return (closestColor, closestPosition);
	}

	public Direct GetNirestColorByOwnColor(Color targetColor)
	{
		double minDiff = double.MaxValue;
		int bestK = -1;
		Color bestColor = Color.None;

		for (int i = 0; i < ownColors.Length; i++)
		{
			Color ownColor = ownColors[i];
			double diff = targetColor.SumDiff(ownColor);
			if (diff < minDiff)
			{
				minDiff = diff;
				bestK = i;
				bestColor = ownColor;
			}
		}

		return new Direct(bestK, bestColor);
	}
	public Mix GetNirestColorByCreateable(Color targetColor)
	{
		double minDiff = double.MaxValue;
		Mix bestRecipe = null;
		var creatableColorsByExist = GetCreatableColorsByExist();

		for (int i = 0; i < creatableColorsByExist.Count; i++)
		{
			Color c = creatableColorsByExist[i].Item1;
			double diff = targetColor.SumDiff(c);
			if (diff < minDiff)
			{
				minDiff = diff;
				bestRecipe = creatableColorsByExist[i].Item2;
			}
		}

		var creatableColors = GetCreatableColors();

		for (int i = 0; i < creatableColors.Count; i++)
		{
			Color c = creatableColors[i].Item1;
			double diff = targetColor.SumDiff(c);
			if (diff < minDiff)
			{
				minDiff = diff;
				bestRecipe = creatableColors[i].Item2;
			}
		}

		return bestRecipe;
	}

	public Color this[int x, int y]
	{
		get => Grid[x, y];
		set => Grid[x, y] = value;
	}

	public override string ToString()
	{
		var result = new StringBuilder((N * 2 + N) * 2);

		for (int i = 0; i < N; i++)
		{
			result.Append(verticalWall[i, 0] ? '1' : '0');
			for (int j = 1; j < N - 1; j++)
			{
				result.Append(verticalWall[i, j] ? " 1" : " 0");
			}
			result.AppendLine();
		}

		for (int i = 0; i < N - 1; i++)
		{
			result.Append(horizontalWall[i, 0] ? '1' : '0');
			for (int j = 1; j < N; j++)
			{
				result.Append(horizontalWall[i, j] ? " 1" : " 0");
			}
			result.AppendLine();
		}

		return result.ToString();
	}
}

public struct Color : IEqualityComparer<Color>, IEquatable<Color>
{
	public static readonly Color None = new Color(-1, -1, -1);
	public double R { get; set; }
	public double G { get; set; }
	public double B { get; set; }
	public double W { get; set; }
	public double SquaredNorm => R * R + G * G + B * B;
	public Color(double r, double g, double b, double w = 1.0)
	{
		R = r;
		G = g;
		B = b;
		W = w;
	}

	public readonly double SumDiff(Color other)
	{
		double r = R - other.R;
		double g = G - other.G;
		double b = B - other.B;
		return Math.Abs(r) + Math.Abs(g) + Math.Abs(b);
	}

	public readonly Color Marge(Color other)
	{
		if (this == None)
		{
			return other;
		}

		if (other == None)
		{
			return this;
		}

		return new Color(
			(R + other.R) / (W + other.W),
			(G + other.G) / (W + other.W),
			(B + other.B) / (W + other.W),
			W + other.W
		);
	}

	public void Sub(double w)
	{
		W -= w;
		if (W < 0.0000001)
		{
			this = None;
		}
	}

	public override readonly string ToString()
	{
		return $"{R:F6} {G:F6} {B:F6}";
	}

	public static bool operator ==(Color left, Color right)
	{
		return (Math.Abs(left.R - right.R) <= 0.0000001) &&
			   (Math.Abs(left.G - right.G) <= 0.0000001) &&
			   (Math.Abs(left.B - right.B) <= 0.0000001);
	}

	public static bool operator !=(Color left, Color right)
	{
		return !(left == right);
	}

	public override readonly bool Equals(object? obj)
	{
		if (obj is Color other)
		{
			return this == other;
		}
		return false;
	}

	public static explicit operator Color((double r, double g, double b) tuple)
	{
		return new Color(tuple.r, tuple.g, tuple.b);
	}

	public static implicit operator (double r, double g, double b)(Color color)
	{
		return (color.R, color.G, color.B);
	}

	public override readonly int GetHashCode()
	{
		unchecked
		{
			int hash = 17;
			hash = hash * 31 + R.GetHashCode();
			hash = hash * 31 + G.GetHashCode();
			hash = hash * 31 + B.GetHashCode();
			return hash;
		}
	}

	public bool Equals(Color x, Color y)
	{
		return x == y;
	}

	public int GetHashCode([DisallowNull] Color obj)
	{
		return obj.R.GetHashCode() ^ obj.G.GetHashCode() ^ obj.B.GetHashCode();
	}

	public bool Equals(Color other)
	{
		return this == other;
	}
}

#region library
#pragma warning disable CA1050

/// <summary>
/// 標準入力の読み取りを簡素化する機能を提供します。
/// </summary>
public static class InputUtil
{
	/// <summary>
	/// 標準入力からスペースで区切られた値を指定の型に変換して読み込みます。
	/// </summary>
	/// <remarks>
	/// 1つの値を読み込むには型を明示し <c>int a = ReadLine&lt;int&gt;()</c> のように書きます。
	/// 定数個の値を読み取るには <c>var (a, b, c) = ReadLine&lt;int&gt;();</c> のように書きます。
	/// 可変個の値を読み取るには <c>foreach (var item in ReadLine&lt;int&gt;())</c> のように書きます。
	/// <c>ToArray()</c> メソッドや Linq も使えます。
	/// </remarks>
	/// <typeparam name="T">変換先の型</typeparam>
	/// <returns>標準入力の読み取り結果。</returns>
	/// <exception cref="FormatException"></exception>
	/// <exception cref="InvalidOperationException"></exception>
	public static InputToken<T, SpanParsableImpl<T>> ReadLine<T>() where T : ISpanParsable<T>
	{
		return new InputToken<T, SpanParsableImpl<T>>(Console.ReadLine() ?? throw new InvalidOperationException());
	}

	/// <summary>
	/// 標準入力から指定の文字で区切られた値を指定の型に変換して読み込みます。
	/// 使用方法は <see cref="ReadLine{T}"/> を参照してください。
	/// </summary>
	/// <typeparam name="T"></typeparam>
	/// <param name="formatProvider"></param>
	/// <param name="separator"></param>
	/// <returns></returns>
	/// <exception cref="InvalidOperationException"></exception>
	public static InputToken<T, SpanParsableImpl<T>> ReadLine<T>(IFormatProvider formatProvider, char separator) where T : ISpanParsable<T>
	{
		return new InputToken<T, SpanParsableImpl<T>>(Console.ReadLine() ?? throw new InvalidOperationException(), formatProvider, separator);
	}

	/// <summary>
	/// 標準入力からスペースで区切られた文字列を読み込みます。
	/// 使用方法は <see cref="ReadLine{T}"/> を参照してください。
	/// </summary>
	/// <returns></returns>
	/// <exception cref="InvalidOperationException"></exception>
	public static InputToken<string, StringImpl> ReadLine()
	{
		return new InputToken<string, StringImpl>(Console.ReadLine() ?? throw new InvalidOperationException());
	}

	/// <summary>
	/// 標準入力から指定の文字で区切られた文字列を読み込みます。
	/// 使用方法は <see cref="ReadLine{T}"/> を参照してください。
	/// </summary>
	/// <param name="formatProvider"></param>
	/// <param name="separator"></param>
	/// <returns></returns>
	/// <exception cref="InvalidOperationException"></exception>
	public static InputToken<string, StringImpl> ReadLine(IFormatProvider formatProvider, char separator)
	{
		return new InputToken<string, StringImpl>(Console.ReadLine() ?? throw new InvalidOperationException(), formatProvider, separator);
	}
}

public interface IReadNextValueImpl<TResult>
{
	public static abstract TResult ReadNextValue(string input, ref int currentIndex, char separator, IFormatProvider formatProvider);

	public static abstract bool TryReadNextValue(string input, ref int currentIndex, char separator, IFormatProvider formatProvider, out TResult value);
}

public readonly struct SpanParsableImpl<T> : IReadNextValueImpl<T> where T : ISpanParsable<T>
{
	public static T ReadNextValue(string input, ref int currentIndex, char separator, IFormatProvider formatProvider)
	{
		ReadOnlySpan<char> span = input.AsSpan()[currentIndex..];
		var index = span.IndexOf(separator);
		ReadOnlySpan<char> target = index == -1 ? span : span[..index];
		if (target.Length == 0)
		{
			ThrowSeparatorNotFound();
		}
		var value = T.Parse(target, formatProvider);
		currentIndex = index == -1 ? input.Length : currentIndex + index + 1;
		return value;
	}

	private static void ThrowSeparatorNotFound()
	{
		throw new FormatException($"Separator not found");
	}

	public static bool TryReadNextValue(string input, ref int currentIndex, char separator, IFormatProvider formatProvider, out T value)
	{
		ReadOnlySpan<char> span = input.AsSpan()[currentIndex..];
		var index = span.IndexOf(separator);
		ReadOnlySpan<char> target = index == -1 ? span : span[..index];
		if (target.Length == 0)
		{
			value = default!;
			return false;
		}
		value = T.Parse(target, formatProvider);
		currentIndex = index == -1 ? input.Length : currentIndex + index + 1;
		return true;
	}
}

public readonly struct StringImpl : IReadNextValueImpl<string>
{
	public static string ReadNextValue(string input, ref int currentIndex, char separator, IFormatProvider formatProvider)
	{
		ReadOnlySpan<char> span = input.AsSpan()[currentIndex..];
		var index = span.IndexOf(separator);
		ReadOnlySpan<char> target = index == -1 ? span : span[..index];
		if (target.Length == 0)
		{
			ThrowSeparatorNotFound();
		}
		var value = target.ToString();
		currentIndex = index == -1 ? input.Length : currentIndex + index + 1;
		return value;
	}

	private static void ThrowSeparatorNotFound()
	{
		throw new FormatException($"Separator not found");
	}

	public static bool TryReadNextValue(string input, ref int currentIndex, char separator, IFormatProvider formatProvider, out string value)
	{
		ReadOnlySpan<char> span = input.AsSpan()[currentIndex..];
		var index = span.IndexOf(separator);
		ReadOnlySpan<char> target = index == -1 ? span : span[..index];
		if (target.Length == 0)
		{
			value = default!;
			return false;
		}
		value = target.ToString();
		currentIndex = index == -1 ? input.Length : currentIndex + index + 1;
		return true;
	}
}

public struct InputToken<TResult, TImpl> : IEnumerable<TResult>, IEnumerator<TResult> where TImpl : IReadNextValueImpl<TResult>
{
	private readonly string _input;

	private int _currentIndex;

	private readonly IFormatProvider _formatProvider;

	private readonly char _separator;

#pragma warning disable CS8618 // Property Current is initialized in MoveNext
	public InputToken(string input)
	{
		_input = input;
		_formatProvider = System.Globalization.CultureInfo.InvariantCulture;
		_separator = ' ';
	}

	public InputToken(string input, IFormatProvider formatProvider, char separator)
	{
		_input = input;
		_formatProvider = formatProvider;
		_separator = separator;
	}
#pragma warning restore CS8618

	public static implicit operator TResult(InputToken<TResult, TImpl> token)
	{
		return token.ReadNextValue();
	}

	public void Deconstruct(out TResult val1, out TResult val2)
	{
		val1 = ReadNextValue();
		val2 = ReadNextValue();
	}

	public void Deconstruct(out TResult val1, out TResult val2, out TResult val3)
	{
		val1 = ReadNextValue();
		val2 = ReadNextValue();
		val3 = ReadNextValue();
	}

	public void Deconstruct(out TResult val1, out TResult val2, out TResult val3, out TResult val4)
	{
		val1 = ReadNextValue();
		val2 = ReadNextValue();
		val3 = ReadNextValue();
		val4 = ReadNextValue();
	}

	public void Deconstruct(out TResult val1, out TResult val2, out TResult val3, out TResult val4, out TResult val5)
	{
		val1 = ReadNextValue();
		val2 = ReadNextValue();
		val3 = ReadNextValue();
		val4 = ReadNextValue();
		val5 = ReadNextValue();
	}

	public void Deconstruct(out TResult val1, out TResult val2, out TResult val3, out TResult val4, out TResult val5, out TResult val6)
	{
		val1 = ReadNextValue();
		val2 = ReadNextValue();
		val3 = ReadNextValue();
		val4 = ReadNextValue();
		val5 = ReadNextValue();
		val6 = ReadNextValue();
	}

	public void Deconstruct(out TResult val1, out TResult val2, out TResult val3, out TResult val4, out TResult val5, out TResult val6, out TResult val7)
	{
		val1 = ReadNextValue();
		val2 = ReadNextValue();
		val3 = ReadNextValue();
		val4 = ReadNextValue();
		val5 = ReadNextValue();
		val6 = ReadNextValue();
		val7 = ReadNextValue();
	}

	public void Deconstruct(out TResult val1, out TResult val2, out TResult val3, out TResult val4, out TResult val5, out TResult val6, out TResult val7, out TResult val8)
	{
		val1 = ReadNextValue();
		val2 = ReadNextValue();
		val3 = ReadNextValue();
		val4 = ReadNextValue();
		val5 = ReadNextValue();
		val6 = ReadNextValue();
		val7 = ReadNextValue();
		val8 = ReadNextValue();
	}

	private TResult ReadNextValue()
	{
		return TImpl.ReadNextValue(_input, ref _currentIndex, _separator, _formatProvider);
	}

	public readonly InputToken<TResult, TImpl> GetEnumerator()
	{
		return this;
	}

	public TResult Current { get; private set; }

	readonly object IEnumerator.Current => Current!;

	public bool MoveNext()
	{
		var val = TImpl.TryReadNextValue(_input, ref _currentIndex, _separator, _formatProvider, out TResult? current);
		Current = current;
		return val;
	}

	public TResult[] ToArray()
	{
		if (_input.Length == 0)
		{
			return Array.Empty<TResult>();
		}
		ref var begin = ref Unsafe.As<char, ushort>(ref MemoryMarshal.GetReference(_input.AsSpan()));
		var count = SpanHelpers.CountValueType(ref begin, _separator, _input.Length) + (_input[^1] == _separator ? 0 : 1);
		var array = new TResult[count];
		for (var i = 0; i < array.Length; i++)
		{
			array[i] = ReadNextValue();
		}
		return array;
	}

	readonly IEnumerator<TResult> IEnumerable<TResult>.GetEnumerator()
	{
		return this;
	}

	readonly IEnumerator IEnumerable.GetEnumerator()
	{
		return this;
	}

	void IEnumerator.Reset()
	{
		_currentIndex = 0;
	}

	readonly void IDisposable.Dispose()
	{

	}
}

// Source: [System.Private.CoreLib]System.SpanHelpers
internal static class SpanHelpers
{
	public static int CountValueType<T>(ref T current, T value, int length) where T : struct, IEquatable<T>?
	{
		var count = 0;
		ref T end = ref Unsafe.Add(ref current, length);

		if (Vector128.IsHardwareAccelerated && length >= Vector128<T>.Count)
		{
			// Vector512 is not supported on .NET 7.0 so Vector512 code is not included.
			if (Vector256.IsHardwareAccelerated && length >= Vector256<T>.Count)
			{
				var targetVector = Vector256.Create(value);
				ref T oneVectorAwayFromEnd = ref Unsafe.Subtract(ref end, Vector256<T>.Count);
				do
				{
					count += BitOperations.PopCount(Vector256.Equals(Vector256.LoadUnsafe(ref current), targetVector).ExtractMostSignificantBits());
					current = ref Unsafe.Add(ref current, Vector256<T>.Count);
				}
				while (!Unsafe.IsAddressGreaterThan(ref current, ref oneVectorAwayFromEnd));

				// If there are just a few elements remaining, then processing these elements by the scalar loop
				// is cheaper than doing bitmask + popcount on the full last vector. To avoid complicated type
				// based checks, other remainder-count based logic to determine the correct cut-off, for simplicity
				// a half-vector size is chosen (based on benchmarks).
				var remaining = (uint)Unsafe.ByteOffset(ref current, ref end) / (uint)Unsafe.SizeOf<T>();
				if (remaining > Vector256<T>.Count / 2)
				{
					var mask = Vector256.Equals(Vector256.LoadUnsafe(ref oneVectorAwayFromEnd), targetVector).ExtractMostSignificantBits();

					// The mask contains some elements that may be double-checked, so shift them away in order to get the correct pop-count.
					var overlaps = (uint)Vector256<T>.Count - remaining;
					mask >>= (int)overlaps;
					count += BitOperations.PopCount(mask);

					return count;
				}
			}
			else
			{
				var targetVector = Vector128.Create(value);
				ref T oneVectorAwayFromEnd = ref Unsafe.Subtract(ref end, Vector128<T>.Count);
				do
				{
					count += BitOperations.PopCount(Vector128.Equals(Vector128.LoadUnsafe(ref current), targetVector).ExtractMostSignificantBits());
					current = ref Unsafe.Add(ref current, Vector128<T>.Count);
				}
				while (!Unsafe.IsAddressGreaterThan(ref current, ref oneVectorAwayFromEnd));

				var remaining = (uint)Unsafe.ByteOffset(ref current, ref end) / (uint)Unsafe.SizeOf<T>();
				if (remaining > Vector128<T>.Count / 2)
				{
					var mask = Vector128.Equals(Vector128.LoadUnsafe(ref oneVectorAwayFromEnd), targetVector).ExtractMostSignificantBits();

					// The mask contains some elements that may be double-checked, so shift them away in order to get the correct pop-count.
					var overlaps = (uint)Vector128<T>.Count - remaining;
					mask >>= (int)overlaps;
					count += BitOperations.PopCount(mask);

					return count;
				}
			}
		}

		while (Unsafe.IsAddressLessThan(ref current, ref end))
		{
			if (current.Equals(value))
			{
				count++;
			}

			current = ref Unsafe.Add(ref current, 1);
		}

		return count;
	}
}

#endregion
