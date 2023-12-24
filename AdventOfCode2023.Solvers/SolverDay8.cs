namespace AdventOfCode2023.Solvers;

public class SolverDay8 : SolverBase
{
	public SolverDay8()
		: base(8, "Haunted Wasteland")
	{ }

    public override ulong Part1(string[] lines)
    {
		string instructions = lines[0];
		var map = new Dictionary<string, Tuple<string, string>>();
	
		foreach (var line in lines[2..]) {
			var lineParts = line.Split(" = ");
			string key = lineParts[0];
			string from = lineParts[1].Substring(1, 3);
			string to = lineParts[1].Substring(6, 3);

			map.Add(key, Tuple.Create(from, to));
		}

		string currentPosition = "AAA";
		ulong i;

		for (i = 0; currentPosition != "ZZZ"; ++i)
			currentPosition = instructions[(int) i%instructions.Length] == 'L' ?
									map[currentPosition].Item1: map[currentPosition].Item2;

		return i;
    }

    public override ulong Part2(string[] lines)
    {
		string instructions = lines[0];
		var map = new Dictionary<string, Tuple<string, string>>();
		var paths = new Dictionary<string, Tuple<ulong, ulong>>();
	
		foreach (var line in lines[2..]) {
			var lineParts = line.Split(" = ");
			string key = lineParts[0];
			string from = lineParts[1].Substring(1, 3);
			string to = lineParts[1].Substring(6, 3);

			map.Add(key, Tuple.Create(from, to));
			if (key[2] == 'A')
				paths.Add(key, Tuple.Create(0UL, 0UL));
		}

		string biggestCycleKey = paths.Keys.First();
		foreach (var startPosition in paths.Keys) {
			string currentPosition = startPosition;
			ulong initialPathLength;

			for (initialPathLength = 0; currentPosition[2] != 'Z'; ++initialPathLength) {
				currentPosition = instructions[(int) initialPathLength%instructions.Length] == 'L' ?
										map[currentPosition].Item1: map[currentPosition].Item2;
			}

			ulong cycleLength;
			currentPosition = instructions[(int) initialPathLength%instructions.Length] == 'L' ?
										map[currentPosition].Item1: map[currentPosition].Item2;
			for (cycleLength = 1; currentPosition[2] != 'Z'; ++cycleLength) {
				currentPosition = instructions[(int) cycleLength%instructions.Length] == 'L' ?
										map[currentPosition].Item1: map[currentPosition].Item2;
			}
			paths[startPosition] = Tuple.Create(initialPathLength, cycleLength);

			if (paths[biggestCycleKey].Item2 < cycleLength)
				biggestCycleKey = startPosition;
		}

		for (ulong i = 1; i < 1000000000UL; ++i) {
			ulong steps = paths[biggestCycleKey].Item1 + paths[biggestCycleKey].Item2*i;

			if (paths.All(x => (steps - x.Value.Item1)%x.Value.Item2 == 0))
				return steps;
		}

		return 0UL;
    }
}
