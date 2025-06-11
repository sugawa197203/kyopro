using System;
using System.Collections;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Runtime.Intrinsics;
using System.Text;

namespace Highest;

public static class Program
{
	public static void _Main()
	{
		var (N, K, H, T, D) = InputUtil.ReadLine<uint>();
		Color[] targetColors = new Color[H];
		Palette palette = new((int)N);
		SortedDictionary<Color, int> ownColorSet = new();

		for (int i = 0; i < K; i++)
		{
			var (r, g, b) = InputUtil.ReadLine<double>();
			ownColorSet[new(r, g, b)] = i;
		}



		for (int i = 0; i < H; i++)
		{
			var (r, g, b) = InputUtil.ReadLine<double>();
			targetColors[i] = new Color(r, g, b);
		}

		// 初期状態
		Console.Write(palette.ToString());
		double sumdiff = 0;
		// とりあえず近い色出す
		foreach (var targetColor in targetColors)
		{
			var closestColor = FindClosestColor(targetColor, ownColorSet);
			double r = closestColor.Key.R;
			double g = closestColor.Key.G;
			double b = closestColor.Key.B;
			sumdiff += Math.Sqrt((r - targetColor.R) * (r - targetColor.R) +
								 (g - targetColor.G) * (g - targetColor.G) +
								 (b - targetColor.B) * (b - targetColor.B));
			Console.WriteLine($"1 1 1 {closestColor.Value}");
			Console.WriteLine("2 1 1");
		}
		Console.Error.WriteLine($"sumdiff: {sumdiff}");
	}

	public static KeyValuePair<Color, int> FindClosestColor(Color targetColor, SortedDictionary<Color, int> ownColorSet)
	{
		int left, right, mid;
		left = 0;
		right = ownColorSet.Count - 1;
		// Console.Error.WriteLine($"{ownColorSet.Select(kv => kv.Key.ToString()).Aggregate((a, b) => $"{a} --- {b}")}");
		while (left < right)
		{
			mid = (left + right) / 2;
			var midColor = ownColorSet.ElementAt(mid).Key;
			// Console.Error.WriteLine($"left: {left}, mid:{mid} right: {right}. {targetColor < midColor}");
			if (targetColor <= midColor)
			{
				right = mid;
			}
			else
			{
				left = mid + 1;
			}
		}

		var leftKV = ownColorSet.ElementAt(left);
		var rightKV = ownColorSet.ElementAt(right);
		// Console.Error.WriteLine($"left: {left}, right: {right}");
		// Console.Error.WriteLine($"left: {leftKV.Key}, right: {rightKV.Key}, target: {targetColor}");

		if (leftKV.Key.SquaredCos(targetColor) >= rightKV.Key.SquaredCos(targetColor))
		{
			return rightKV;
		}
		else
		{
			return leftKV;
		}
	}
}

public class Palette
{
	public Color[,] Grid { get; }
	public bool[,] horizontalWall { get; }
	public bool[,] verticalWall { get; }
	private int N;

	public Palette(int n)
	{
		N = n;
		Grid = new Color[n, n];
		horizontalWall = new bool[n, n - 1];
		verticalWall = new bool[n - 1, n];
	}

	public Color this[int x, int y]
	{
		get => Grid[x, y];
		set => Grid[x, y] = value;
	}

	public override string ToString()
	{
		var result = new StringBuilder((N * 2 + N) * 2);

		for (int i = 0; i < N - 1; i++)
		{
			result.Append(verticalWall[i, 0] ? '1' : '0');
			for (int j = 1; j < N; j++)
			{
				result.Append(verticalWall[i, j] ? " 1" : " 0");
			}
			result.AppendLine();
		}

		for (int i = 0; i < N; i++)
		{
			result.Append(horizontalWall[i, 0] ? '1' : '0');
			for (int j = 1; j < N - 1; j++)
			{
				result.Append(horizontalWall[i, j] ? " 1" : " 0");
			}
			result.AppendLine();
		}

		return result.ToString();
	}
}

public struct Color : IComparable
{
	public double R { get; set; }
	public double G { get; set; }
	public double B { get; set; }
	public double SquaredNorm => R * R + G * G + B * B;
	public Color(double r, double g, double b)
	{
		R = r;
		G = g;
		B = b;
	}

	public double SquaredCos(Color other)
	{
		double product = R * other.R + G * other.G + B * other.B;
		return product * product / (SquaredNorm * other.SquaredNorm);
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

	public static bool operator <(Color left, Color right)
	{
		if (Math.Abs(left.R - right.R) <= 0.0000001)
		{
			if (Math.Abs(left.G - right.G) <= 0.0000001)
			{
				if (Math.Abs(left.B - right.B) <= 0.0000001)
				{
					return false; // left and right are equal
				}
				return left.B < right.B;
			}
			return left.G < right.G;
		}
		return left.R < right.R;
	}

	public static bool operator >(Color left, Color right)
	{
		if (Math.Abs(left.R - right.R) <= 0.0000001)
		{
			if (Math.Abs(left.G - right.G) <= 0.0000001)
			{
				if (Math.Abs(left.B - right.B) <= 0.0000001)
				{
					return false; // left and right are equal
				}
				return left.B > right.B;
			}
			return left.G > right.G;
		}
		return left.R > right.R;
	}

	public static bool operator <=(Color left, Color right)
	{
		return (left == right) || (left < right);
	}

	public static bool operator >=(Color left, Color right)
	{
		return (left == right) || (left > right);
	}

	public override readonly bool Equals(object? obj)
	{
		if (obj is Color other)
		{
			return this == other;
		}
		return false;
	}

	public int CompareTo(object? obj)
	{
		if (obj is Color other)
		{
			if (this == other) return 0;
			if (this < other) return -1;
			return 1;
		}
		throw new ArgumentException("Object is not a Color");
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
