using System.CommandLine;
using AdventOfCode2023.Solvers;

class Program
{
	private static void runSolver(byte day, byte part, FileInfo fileInfo)
    {
		SolverBase solver;

		switch(day) {
			case 1:
				solver = new SolverDay1();
				break;
			case 2:
				solver = new SolverDay2();
				break;
			case 3:
				solver = new SolverDay3();
				break;
			case 4:
				solver = new SolverDay4();
				break;
			case 5:
				solver = new SolverDay5();
				break;
			case 6:
				solver = new SolverDay6();
				break;
			case 7:
				solver = new SolverDay7();
				break;
			default:
				Console.WriteLine($"Solver for day {day} is not implemented!");
				return;
		}

		string[] lines = File.ReadLines(fileInfo.FullName).ToArray();
		if ((part & 1) > 0 || part == 0) {
			ulong result = solver.Part1(lines);
			Console.WriteLine($"Solver for -- Day {solver.Day} - {solver.Title} -- part 1 returned: {result}");
		}
		if ((part & 2) > 0 || part == 0) {
			ulong result = solver.Part2(lines);
			Console.WriteLine($"Solver for -- Day {solver.Day} - {solver.Title} -- part 2 returned: {result}");
		}
	}

	public static async Task<int> Main(params string[] args)
	{
		RootCommand rootCommand = new RootCommand(description: "Calls a problem solver for given day.");
		rootCommand.TreatUnmatchedTokensAsErrors = true;

		var dayOption = new Option<byte>(
				name: "--day",
				description: "Day when problem is given.");
		dayOption.AddAlias("-d");
		dayOption.IsRequired = true;
		rootCommand.AddOption(dayOption);

		var partOption = new Option<byte>(
				name: "--part",
				description: "Part of problem that needs to be solved.");
		partOption.AddAlias("-p");
		rootCommand.AddOption(partOption);

		var inputFileOption = new Option<FileInfo>(
				name: "--file",
				description: "Problem input file.");
		inputFileOption.AddAlias("-f");
		inputFileOption.IsRequired = true;
		rootCommand.AddOption(inputFileOption);

		rootCommand.SetHandler<byte, byte, FileInfo>(runSolver, dayOption, partOption, inputFileOption);

		return await rootCommand.InvokeAsync(args);
	}
}
