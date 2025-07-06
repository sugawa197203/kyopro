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
		var (N, M) = InputUtil.ReadLine<int>();
		var field = ReadField(N);
		var freeCount = N * N - M;
		for (int i = 0; i < freeCount; i++)
		{
			field.SlipPossibility();
			var pos = field.GetMinPossibilityPos();
			field.PlaceStone(pos.X, pos.Y);
			Console.WriteLine($"{pos.X} {pos.Y}");
		}
	}
	
	public static Field ReadField(int n)
	{
		var lines = new string[n];
		for (int i = 0; i < n; i++)
		{
			lines[i] = Console.ReadLine();
		}
		return new Field(n, lines);
	}

	
}

public class Field
{
	public IntVec2 Size {get; private set;}
	public float[,] Possibility {get; private set;}
	public int FreeSpaceCount = 0;
	private bool[,] _field;

	public Field(int n, string[] lines)
	{
		Size = new IntVec2(n, n);
		_field = new bool[n, n];
		Possibility = new float[n, n];
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				_field[i, j] = lines[i][j] == '#';
				if (!_field[i, j])
				{
					FreeSpaceCount++;
					Possibility[i, j] = 1.0f;
				}
				else
				{
					Possibility[i, j] = 0.0f;
				}
			}
		}
	}
	public float[,] RecivePossibility()
	{
		float[,] result = new float[Size.X, Size.Y];
		for (int i = 0; i < Size.X; i++)
		{
			for (int j = 0; j < Size.Y; j++)
			{
				if (_field[i, j])
				{
					result[i, j] = 0.0f;
				}
				else
				{
					bool flag = false;
					foreach (var direct in new IntVec2[] { new IntVec2(0, 1), new IntVec2(1, 0), new IntVec2(0, -1), new IntVec2(-1, 0) })
					{
						if (IsStone(i + direct.X, j + direct.Y))
						{
							flag = true;
							break;
						}
					}

					if (!flag)
					{
						result[i, j] = 0.0f;
						continue;
					}
					
					foreach (var direct in new IntVec2[] { new IntVec2(0, 1), new IntVec2(1, 0), new IntVec2(0, -1), new IntVec2(-1, 0) })
					{
						var pos = new IntVec2(i, j);
						while (!IsStone(pos.X + direct.X, pos.Y + direct.Y))
						{
							pos.X += direct.X;
							pos.Y += direct.Y;
							result[i, j] += Possibility[pos.X, pos.Y];
						}
					}
				}
			}
		}
		return result;
	}
	public void SlipPossibility()
	{
		float[,] newPossibility = new float[Size.X, Size.Y];
		for (int i = 0; i < Size.X; i++)
		{
			for (int j = 0; j < Size.Y; j++)
			{
				if (_field[i, j])
				{
					continue;
				}
				
				foreach (var direct in new IntVec2[] { new IntVec2(0, 1), new IntVec2(1, 0), new IntVec2(0, -1), new IntVec2(-1, 0) })
				{
					var pos = new IntVec2(i, j);
					while(!IsStone(pos.X + direct.X, pos.Y + direct.Y))
					{
						pos.X += direct.X;
						pos.Y += direct.Y;
					}
					newPossibility[pos.X, pos.Y] += Possibility[i, j] * 0.25f;
					if (Possibility[i, j] > 0f && newPossibility[pos.X, pos.Y] <= float.Epsilon)
					{
						newPossibility[pos.X, pos.Y] = float.Epsilon;
					}
				}
			}
		}
		
		for (int i = 0; i < Size.X; i++)
		{
			for (int j = 0; j < Size.Y; j++)
			{
				if (newPossibility[i, j] > float.Epsilon)
					continue;
				
				foreach (var direct in new IntVec2[] { new IntVec2(0, 1), new IntVec2(1, 0), new IntVec2(0, -1), new IntVec2(-1, 0) })
				{
					if (IsStone(i + direct.X, j + direct.Y))
					{
						continue;
					}

					newPossibility[i, j] = 0.0f;
				}
			}
		}
		
		Possibility = newPossibility;
	}

	public IntVec2 GetMinPossibilityPos()
	{
		float minimum = float.MaxValue;
		IntVec2 minPos = IntVec2.Zero;
		List<IntVec2> minPoses = new List<IntVec2>();
		for (int i = 0; i < Size.X; i++)
		{
			for (int j = 0; j < Size.Y; j++)
			{
				if (_field[i, j])
				{
					continue;
				}
				if (Possibility[i, j] < minimum)
				{
					minimum = Possibility[i, j];
					minPos.X = i;
					minPos.Y = j;
				}
			}
		}
		
		for (int i = 0; i < Size.X; i++)
		{
			for (int j = 0; j < Size.Y; j++)
			{
				if (_field[i, j])
				{
					continue;
				}
				if (Math.Abs(Possibility[i, j] - minimum) < float.Epsilon)
				{
					minPoses.Add(new IntVec2(i, j));
				}
			}
		}
		
		if (minPoses.Count == 1)
		{
			var recive = RecivePossibility();
			var min = float.MaxValue;
			for (int i = 0; i < Size.X; i++)
			{
				for (int j = 0; j < Size.Y; j++)
				{
					if (_field[i, j])
					{
						continue;
					}
					if (recive[i, j] < min)
					{
						min = recive[i, j];
						minPos.X = i;
						minPos.Y = j;
					}
				}
			}
			
			return minPos;
		}
		
		float maxAroundPossibility = float.MinValue;
		IntVec2 maxPos = IntVec2.Zero;
		foreach (var pos in minPoses)
		{
			float aroundPossibility = 0.0f;
			foreach (var direct in new IntVec2[] { new IntVec2(0, 1), new IntVec2(1, 0), new IntVec2(0, -1), new IntVec2(-1, 0) })
			{
				if (IsStone(pos.X + direct.X, pos.Y + direct.Y))
				{
					continue;
				}
				aroundPossibility += Possibility[pos.X + direct.X, pos.Y + direct.Y];
			}
			if (aroundPossibility > maxAroundPossibility)
			{
				maxAroundPossibility = aroundPossibility;
				maxPos = pos;
			}
		}
		
		return maxPos;
	}
	
	public void PlaceStone(int x, int y)
	{
		if (x < 0 || x >= Size.X || y < 0 || y >= Size.Y)
		{
			throw new ArgumentOutOfRangeException("Position out of bounds");
		}
		if (!_field[x, y])
		{
			_field[x, y] = true;
			FreeSpaceCount--;
		}
	}

	public List<IntVec2> FreeSpace()
	{
		List<IntVec2> freeSpace = new List<IntVec2>(FreeSpaceCount);
		for (int i = 0; i < Size.X; i++)
		{
			for (int j = 0; j < Size.Y; j++)
			{
				if (!_field[i, j])
				{
					freeSpace.Add(new IntVec2(i, j));
				}
			}
		}
		return freeSpace;
	}
	
	public bool IsStone(int x, int y)
	{
		if (x < 0 || x >= Size.X || y < 0 || y >= Size.Y)
		{
			return true;
		}
		return _field[x, y];
	}

	public int[,] CalcSlipedPos()
	{
		int[,] result = new int[Size.X, Size.Y];
		for (int i = 0; i < Size.X; i++)
		{
			for (int j = 0; j < Size.Y; j++)
			{
				if (IsStone(i, j))
				{
					result[i, j] = int.MaxValue;
					continue;
				}
				
				foreach (var direct in new IntVec2[] { new IntVec2(0, 1), new IntVec2(1, 0), new IntVec2(0, -1), new IntVec2(-1, 0) })
				{
					var pos = new IntVec2(i, j);
					while(!IsStone(pos.X + direct.X, pos.Y + direct.Y))
					{
						pos.X += direct.X;
						pos.Y += direct.Y;
					}
					result[pos.X, pos.Y]++;
				}
			}
		}
		return result;
	}
	
	public float[,] GetPriority()
	{
		var slipedPos = CalcSlipedPos();
		
		// Console.WriteLine("Sliped Positions:");
		// for (int i = 0; i < Size.X; i++)
		// {
		// 	Console.WriteLine(string.Join(" ", Enumerable.Range(0, Size.Y).Select(j => slipedPos[i, j].ToString("D2"))));
		// }
		
		
		float[,] priority = new float[Size.X, Size.Y];
		for (int i = 0; i < Size.X; i++)
		{
			for (int j = 0; j < Size.Y; j++)
			{
				if (IsStone(i, j))
				{
					priority[i, j] = 0.0f;
					continue;
				}

				var roundcount = 0;
				foreach (var direct in new IntVec2[] { new IntVec2(0, 1), new IntVec2(1, 0), new IntVec2(0, -1), new IntVec2(-1, 0) })
				{
					if (IsStone(i + direct.X, j + direct.Y))
					{
						continue;
					}
					
					roundcount += slipedPos[i + direct.X, j + direct.Y];
				}

				if (slipedPos[i, j] == 0)
				{
					priority[i, j] = roundcount;
				}
				else
				{
					// priority[i, j] = (float)roundcount / (float)slipedPos[i, j];
					priority[i, j] = 0;
				}
			}
		}
		return priority;
	}

	public IntVec2 GetMostPriority()
	{
		var priority = GetPriority();
		
		// Console.WriteLine("Priority Map:");
		// for (int i = 0; i < Size.X; i++)
		// {
		// 	Console.WriteLine(string.Join(" ", Enumerable.Range(0, Size.Y).Select(j => priority[i, j].ToString("F2"))));
		// }
		
		float maxPriority = float.MinValue;
		IntVec2 bestPos = IntVec2.Zero;
		for (int i = 0; i < Size.X; i++)
		{
			for (int j = 0; j < Size.Y; j++)
			{
				if (IsStone(i, j))
				{
					continue;
				}
				if (priority[i, j] > maxPriority)
				{
					maxPriority = priority[i, j];
					bestPos.X = i;
					bestPos.Y = j;
				}
			}
		}
		if (maxPriority == float.MinValue)
		{
			throw new InvalidOperationException("No free space available");
		}
		return bestPos;
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
		return $"{X} {Y}";
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
