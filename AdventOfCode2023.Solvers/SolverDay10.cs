namespace AdventOfCode2023.Solvers;

public class SolverDay10 : SolverBase
{
	public SolverDay10()
		: base(10, "Pipe Maze")
	{ }

	private List<Tuple<int, int>>? findPath(string[] lines, Queue<Tuple<int, int>> position)
	{
		var rules = new List<Tuple<char, Tuple<int, int, char[]>[]>>();
		rules.Add(Tuple.Create('|', new[] { Tuple.Create(1, 0, "|LJ".ToArray()), Tuple.Create(-1, 0, "|F7".ToArray()) }));
		rules.Add(Tuple.Create('-', new[] { Tuple.Create(0, 1, "-7J".ToArray()), Tuple.Create(0, -1, "-LF".ToArray()) }));
		rules.Add(Tuple.Create('L', new[] { Tuple.Create(0, 1, "-7J".ToArray()), Tuple.Create(-1, 0, "|F7".ToArray()) }));
		rules.Add(Tuple.Create('J', new[] { Tuple.Create(0, -1, "-LF".ToArray()), Tuple.Create(-1, 0, "|F7".ToArray()) }));
		rules.Add(Tuple.Create('F', new[] { Tuple.Create(1, 0, "|LJ".ToArray()), Tuple.Create(0, 1, "-7J".ToArray()) }));
		rules.Add(Tuple.Create('7', new[] { Tuple.Create(1, 0, "|LJ".ToArray()), Tuple.Create(0, -1, "-LF".ToArray()) }));

		var map = lines.Select(r => r.Select(c => false).ToArray()).ToArray();
		var path = new List<Tuple<int, int>>();

		path.Add(position.Dequeue());
		map[path[0].Item1][path[0].Item2] = true;
		while (position.Any()) {
			(int r, int c) = position.Dequeue();
			map[r][c] = true;
			path.Add(Tuple.Create(r, c));

			foreach ((char currentSymbol, var combinations) in rules) {
				if (lines[r][c] != currentSymbol)
					continue;

				foreach ((int tmpR, int tmpC, char[] pipes) in combinations) {
					int rr = r + tmpR;
					int cc = c + tmpC;

					if (rr < lines.Length && rr >= 0 && cc < lines[rr].Length && cc >= 0 && !map[rr][cc]
							&& pipes.Contains(lines[rr][cc])) {
						position.Enqueue(Tuple.Create(rr, cc));
					}
				}
			}
		}

		if (int.Abs((path.First().Item1 - path.Last().Item1) + (path.First().Item2 - path.Last().Item2)) > 1)
			return null;

        return path;
	}

    public override ulong Part1(string[] lines)
    {
		Tuple<int, int> start = Tuple.Create(-1, -1);
		for(int r = 0; r < lines.Length && start.Item1 == -1; ++r)
			for (int c = 0; c < lines[r].Length && start.Item1 == -1; ++c)
				if (lines[r][c] == 'S')
					start = Tuple.Create(r, c);

		var combinations = new List<Tuple<int, int, char[]>>();
		combinations.Add(Tuple.Create(1, 0, "|LJ".ToArray()));
		combinations.Add(Tuple.Create(-1, 0, "|F7".ToArray()));
		combinations.Add(Tuple.Create(0, 1, "-7J".ToArray()));
		combinations.Add(Tuple.Create(0, -1, "-LF".ToArray()));

		foreach ((int tmpR, int tmpC, char[] pipes) in combinations) {
			int rr = start.Item1 + tmpR;
			int cc = start.Item2 + tmpC;

			if (rr < lines.Length && rr >= 0 && cc < lines[rr].Length && cc >= 0 && pipes.Contains(lines[rr][cc])) {
				var startPath = new Queue<Tuple<int, int>>();

				startPath.Enqueue(start);
				startPath.Enqueue(Tuple.Create(rr, cc));
				var path = findPath(lines, startPath);
				if (path != null)
					return (ulong) path.Count()/2UL;
			}
		}

		return 0;
    }

    public override ulong Part2(string[] lines)
    {
		Tuple<int, int> start = Tuple.Create(-1, -1);
		for(int r = 0; r < lines.Length && start.Item1 == -1; ++r)
			for (int c = 0; c < lines[r].Length && start.Item1 == -1; ++c)
				if (lines[r][c] == 'S')
					start = Tuple.Create(r, c);

		var combinations = new List<Tuple<int, int, char[]>>();
		combinations.Add(Tuple.Create(1, 0, "|LJ".ToArray()));
		combinations.Add(Tuple.Create(-1, 0, "|F7".ToArray()));
		combinations.Add(Tuple.Create(0, 1, "-7J".ToArray()));
		combinations.Add(Tuple.Create(0, -1, "-LF".ToArray()));

		foreach ((int tmpR, int tmpC, char[] pipes) in combinations) {
			int rr = start.Item1 + tmpR;
			int cc = start.Item2 + tmpC;

			if (rr < lines.Length && rr >= 0 && cc < lines[rr].Length && cc >= 0 && pipes.Contains(lines[rr][cc])) {
				var startPath = new Queue<Tuple<int, int>>();

				startPath.Enqueue(start);
				startPath.Enqueue(Tuple.Create(rr, cc));
				var path = findPath(lines, startPath);
				if (path != null) {
					long area = 0;
					for (int i = 0; i < path.Count(); ++i) {
						var nextI = (i + 1)%path.Count();
						long part = (long) (path[i].Item1*path[nextI].Item2 - path[i].Item2*path[nextI].Item1);
						area += part;
					}
					return (ulong) (long.Abs(area)/2L - path.Count()/2L + 1L);
				}
			}
		}

		return 0;
    }
}
