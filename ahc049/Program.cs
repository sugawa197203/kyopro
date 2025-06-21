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
		int N = InputUtil.ReadLine<int>();
		var field = ReadPackages(N);
		var pos = new IntVec2(0, 0);
		
		for (int i = N - 1; i >= 0; i--)
		{
			for (int j = N - 1; j >= 0; j--)
			{
				IntVec2 tartget = new IntVec2(i, j);
				if (!field.Contain(tartget))
				{
					continue;
				}

				if (i == 0 && j == 0)
				{
					continue;
				}

				Move(pos, tartget);
				pos = tartget;
				Console.WriteLine("1");
				var package = field.PickUpPackage(tartget);
				MoveWithPickUp(pos, field, package);
				pos = IntVec2.Zero;
			}
		}
	}

	public static Field ReadPackages(int N)
	{
		Package[][] packages = new Package[N][];
		for (int i = 0; i < N; i++)
		{
			packages[i] = new Package[N];
		}

		for (int i = 0; i < N; i++)
		{
			int[] weights = InputUtil.ReadLine<int>().ToArray();
			for (int j = 0; j < weights.Length; j++)
			{
				packages[i][j] = new Package(weights[j], 0, new IntVec2(i, j));
			}
		}

		for (int i = 0; i < N; i++)
		{
			int[] protections = InputUtil.ReadLine<int>().ToArray();
			for (int j = 0; j < protections.Length; j++)
			{
				packages[i][j].Protection = protections[j];
			}
		}

		packages[0][0] = null;

		return new Field(packages, N);
	}

	public static void Move(IntVec2 from, IntVec2 to)
	{
		// x move
		while (from.X != to.X)
		{
			if (from.X < to.X)
			{
				from.X++;
				Console.WriteLine("R");
			}
			else
			{
				from.X--;
				Console.WriteLine("L");
			}
		}

		// y move
		while (from.Y != to.Y)
		{
			if (from.Y < to.Y)
			{
				from.Y++;
				Console.WriteLine("D");
			}
			else
			{
				from.Y--;
				Console.WriteLine($"U");
			}
		}
	}

	public static void MoveWithPickUp(IntVec2 from, Field field, Package having)
	{
		var pos = from;
		// x move
		while (pos.X != 0)
		{
			pos.X--;
			Console.WriteLine("L");
			if (field.Contain(pos))
			{
				var package = field[pos];
				if (package.Cost < having.Protection)
				{
					field.PickUpPackage(pos);
					Console.WriteLine("1");
					Move(pos, IntVec2.Zero);
					return;
				}
			}
		}
		
		// y move
		while (pos.Y != 0)
		{
			pos.Y--;
			Console.WriteLine($"U");
			if (field.Contain(pos))
			{
				var package = field[pos];
				if (package.Cost < having.Protection)
				{
					field.PickUpPackage(pos);
					Console.WriteLine("1");
					Move(pos, IntVec2.Zero);
					return;
				}
			}
		}

	}

}

public class Field
{
	private Package?[][] _packages;
	private int _size;

	public Field(Package[][] packages, int size)
	{
		_packages = packages;
		_size = size;
	}

	public Package this[int i, int j]
	{
		get => _packages[i][j];
		set => _packages[i][j] = value;
	}
	
	public Package this[IntVec2 vec2]
	{
		get => _packages[vec2.Y][vec2.X];
		set => _packages[vec2.Y][vec2.X] = value;
	}
	
	public int Size => _size;
	
	public void Place(int i, int j, Package package)
	{
		if (_packages[i][j] != null)
		{
			throw new InvalidOperationException("Package already exists at this position.");
		}
		_packages[i][j] = package;
	}

	public void Place(IntVec2 vec2, Package package)
	{
		Place(vec2.X, vec2.Y, package);
	}

	public Package PickUpPackage(int i, int j)
	{
		if (_packages[i][j] == null)
		{
			throw new InvalidOperationException("No package at this position.");
		}
		var package = _packages[i][j];
		_packages[i][j] = null;
		return package;
	}
	
	public Package PickUpPackage(IntVec2 vec2)
	{
		return PickUpPackage(vec2.Y, vec2.X);
	}
	
	public bool Contain(int i, int j)
	{
		return _packages[i][j] != null;
	}
	
	public bool Contain(IntVec2 vec2)
	{
		return Contain(vec2.Y, vec2.X);
	}
}

public class Package
{
	private int _weight;
	private int _protection;
	private IntVec2 _pos;

	public int Weight
	{
		get => _weight;
		set => _weight = value;
	}

	public int Protection
	{
		get => _protection;
		set => _protection = value;
	}
	
	public int Cost
	{
		get => _weight * _pos.GetManhattan;
	}
	
	public IntVec2 Position
	{
		get => _pos;
		set => _pos = value;
	}

	public Package(int weight, int protection, IntVec2 pos)
	{
		_weight = weight;
		_protection = protection;
		_pos = pos;
	}
}

public struct IntVec2
{
	public static readonly IntVec2 Zero = new IntVec2(0, 0);
	int _x;
	int _y;
	public int X
	{
		get => _x;
		set => _x = value;
	}
	public int Y
	{
		get => _y;
		set => _y = value;
	}
	
	public int GetManhattan => _x + _y + 2;
	public IntVec2(int x, int y)
	{
		_x = x;
		_y = y;
	}

	public IntVec2()
	{
		_x = -1;
		_y = -1;
	}
	
	public override string ToString()
	{
		return $"{{{X}, {Y}}}";
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
