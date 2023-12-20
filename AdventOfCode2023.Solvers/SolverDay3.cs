namespace AdventOfCode2023.Solvers;

public class SolverDay3 : SolverBase
{
	public SolverDay3()
		: base(3, "Gear Ratios")
	{ }

	override public ulong Part1(string[] lines)
	{
		ulong number;
		bool isPartNumber;
		ulong sumPartNumbers = 0;

		for (int r = 0; r < lines.Length; ++r) {
			number = 0;
			isPartNumber = false;

			for (int c = 0; c < lines[r].Length; ++c) {
				if (lines[r][c] < '0' || lines[r][c] > '9') {
					if (isPartNumber)
						sumPartNumbers += number;

					number = 0;
					isPartNumber = false;
					continue;
				}

				number = number*10 + lines[r][c] - '0';
				for (int i = 0; i < 9 && !isPartNumber; ++i) {
					int rr = r + (i/3 - 1);
					int cc = c + (i%3 - 1);

					if (rr >= 0 && rr < lines.Length &&
							cc >= 0 && cc < lines[r].Length)
						isPartNumber = isPartNumber ||
							(lines[rr][cc] != '.' && (lines[rr][cc] < '0' || lines[rr][cc] > '9'));
				}
			}

			if (isPartNumber)
				sumPartNumbers += number;
		}

		return sumPartNumbers;
	}

	override public ulong Part2(string[] lines)
	{
		uint number;
		uint coords;
		var gears = new Dictionary<uint, List<uint>>();
		ulong sumPartNumbers = 0;

		for (int r = 0; r < lines.Length; ++r) {
			number = 0;
			coords = ~((uint) 0);

			for (int c = 0; c < lines[r].Length; ++c) {
				if (lines[r][c] < '0' || lines[r][c] > '9') {
					if (coords < ~((uint) 0))
						gears[coords].Add(number);

					number = 0;
					coords = ~((uint) 0);
					continue;
				}

				number = number*10 + lines[r][c] - '0';
				for (int i = 0; i < 9 && coords == ~((uint) 0); ++i) {
					int rr = r + (i/3 - 1);
					int cc = c + (i%3 - 1);

					if (rr >= 0 && rr < lines.Length &&
							cc >= 0 && cc < lines[r].Length && lines[rr][cc] == '*') {
						coords = (uint)((rr << 16) + cc);

						if (!gears.Keys.Contains(coords))
							gears.Add(coords, new List<uint>());
					}
				}
			}

			if (coords < ~((uint) 0))
				gears[coords].Add(number);
		}

		foreach (var parts in gears.Values) {
			if (parts.Count() == 2)
				sumPartNumbers += parts[0]*parts[1];
		}

		return sumPartNumbers;
	}
}
