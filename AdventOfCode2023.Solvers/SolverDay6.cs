namespace AdventOfCode2023.Solvers;

public class SolverDay6 : SolverBase
{
	public SolverDay6()
		: base(6, "Wait For It")
	{}

	private ulong nWaysToWin(ulong time, ulong distance)
	{
		ulong l = 1U;
		ulong h = (time + 1U)/2U;

		while(l + 1 < h) {
			ulong m = (l + h)/2;

			if (m*(time - m) <= distance) {
				l = m;
			} else {
				h = m;
			}
		}

		return time - (h*2 - 1);
	}

    public override ulong Part1(string[] lines)
    {
		ulong[] times = lines[0].Substring(9)
							.Split()
							.Where(x => x.Length > 0)
							.Select(x => ulong.Parse(x))
							.ToArray();
		ulong[] distances = lines[1].Substring(9)
							.Split()
							.Where(x => x.Length > 0)
							.Select(x => ulong.Parse(x))
							.ToArray();
		ulong productWaysToWin = 1UL;

		for (int i = 0; i < times.Length; ++i)
			productWaysToWin *= nWaysToWin(times[i], distances[i]);

        return productWaysToWin;
    }

    public override ulong Part2(string[] lines)
    {
		ulong time = ulong.Parse(lines[0].Substring(9).Replace(" ", ""));
		ulong distance = ulong.Parse(lines[1].Substring(9).Replace(" ", ""));

        return nWaysToWin(time, distance);
	}
}
