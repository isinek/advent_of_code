namespace AdventOfCode2023.Solvers;

public struct Range {
	public ulong Start;
	public ulong End;

	public Range(ulong start, ulong end)
	{
		this.Start = start;
		this.End = end;
	}
}

public class SolverDay5 : SolverBase
{
	public SolverDay5()
		: base(5, "If You Give A Seed A Fertilizer")
	{}

	private ulong[] transformValues(ulong[] values, ulong destination, ulong source, ulong range,
			ulong[] transformedValues)
	{
		for (int i = 0; i < values.Length; ++i) {
			if (values[i] >= source && values[i] < source + range)
				transformedValues[i] = values[i] - source + destination;
		}

		return transformedValues;
	}

	private (List<Range> oldRanges, List<Range> newRanges) transformRanges(List<Range> oldRanges, ulong destination,
			ulong source, ulong range, List<Range> newRanges)
	{
		int i = 0;
		ulong sourceEnd = source + range - 1;
		ulong destinationEnd = destination + range - 1;

		while (i < oldRanges.Count) {
			var oldRange = oldRanges[i];
			if (oldRange.Start > sourceEnd || oldRange.End < source) {
				++i;
				continue;
			}

			oldRanges.Remove(oldRange);
			newRanges.Add(new Range(ulong.Max(oldRange.Start, source) - source + destination,
						destinationEnd - (sourceEnd - ulong.Min(oldRange.End, sourceEnd))));

			if (oldRange.Start < source)
				oldRanges.Add(new Range(oldRange.Start, source - 1));
			if (oldRange.End > sourceEnd)
				oldRanges.Add(new Range(sourceEnd + 1, oldRange.End));

			i = 0;
		}

		return (oldRanges, newRanges);
	}

    public override ulong Part1(string[] lines)
    {
		int l = 0;

		var values = lines[l].Split(": ")[1]
					.Split()
					.Select(x => ulong.Parse(x))
					.ToArray();

		l += 3;
		while(l < lines.Count()) {
			var transformedValues = values.Select(x => ~((ulong) 0)).ToArray();

			while (l < lines.Count() && lines[l].Length > 0) {
				var range = lines[l].Split()
									.Select(x => ulong.Parse(x))
									.ToArray();
				transformedValues = transformValues(values, range[0], range[1], range[2], transformedValues);
				++l;
			}

			for (int i = 0; i < values.Length; ++i)
				if (transformedValues[i] < ~((ulong) 0))
					values[i] = transformedValues[i];

			l += 2;
		}
		
        return ((ulong) values.Min());
    }

    public override ulong Part2(string[] lines)
    {
		var rangeInputs = lines[0].Split(": ")[1]
					.Split()
					.Select(x => ulong.Parse(x))
					.ToArray();
		var ranges = new List<Range>();

		for (int r = 0; r < rangeInputs.Length; r += 2)
			ranges.Add(new Range(rangeInputs[r], rangeInputs[r] + rangeInputs[r + 1] - 1));

		int l = 3;
		while(l < lines.Count()) {
			var newRanges = new List<Range>();

			while (l < lines.Count() && lines[l].Length > 0) {
				var range = lines[l].Split()
									.Select(x => ulong.Parse(x))
									.ToArray();
				var result = transformRanges(ranges, range[0], range[1], range[2], newRanges);
				ranges = result.oldRanges;
				newRanges = result.newRanges;
				++l;
			}

			ranges.AddRange(newRanges);

			l += 2;
		}

        return ranges.Select(x => x.Start).Min();
    }
}
