namespace AdventOfCode2023.Solvers;

public class SolverBase
{
	public readonly ushort Day = 0;
	public readonly string Title = "Undefined";

	public SolverBase(ushort day, string title)
	{
		this.Day = day;
		this.Title = title;
	}

	public virtual ulong Part1(string[] lines)
	{
		return 0;
	}

	public virtual ulong Part2(string[] lines)
	{
		return 0;
	}
}

