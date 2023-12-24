namespace AdventOfCode2023.Solvers;

public class SolverDay9 : SolverBase
{
	public SolverDay9()
		: base(9, "Mirage Maintenance")
	{ }

    public override ulong Part1(string[] lines)
    {
		long sumExtrapolatedValues = 0L;

		foreach (var line in lines) {
			var report = new Stack<List<long>>();

			report.Push(line.Split().Select(x => long.Parse(x)).ToList());
			while (report.Peek().Any(x => x != 0L)) {
				var values = report.Peek();
				var diff = new List<long>();

				for (int i = 1; i < values.Count(); ++i) {
					diff.Add(values[i] - values[i - 1]);
				}
				report.Push(diff);
			}

			report.Pop();
			long extrapolatedValue = 0L;
			while (report.Any()) {
				var values = report.Pop();

				extrapolatedValue = values.Last() + extrapolatedValue;
			}

			sumExtrapolatedValues += extrapolatedValue;
		}

        return (ulong) sumExtrapolatedValues;
    }

    public override ulong Part2(string[] lines)
    {
		long sumExtrapolatedValues = 0L;

		foreach (var line in lines) {
			var report = new Stack<List<long>>();

			report.Push(line.Split().Select(x => long.Parse(x)).Reverse().ToList());
			while (report.Peek().Any(x => x != 0L)) {
				var values = report.Peek();
				var diff = new List<long>();

				for (int i = 1; i < values.Count(); ++i) {
					diff.Add(values[i] - values[i - 1]);
				}
				report.Push(diff);
			}

			report.Pop();
			long extrapolatedValue = 0L;
			while (report.Any()) {
				var values = report.Pop();

				extrapolatedValue = values.Last() + extrapolatedValue;
			}

			sumExtrapolatedValues += extrapolatedValue;
		}

        return (ulong) sumExtrapolatedValues;
    }
}
