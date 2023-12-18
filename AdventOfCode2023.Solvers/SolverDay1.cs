namespace AdventOfCode2023.Solvers;

public class SolverDay1 : SolverBase
{
	public SolverDay1()
		: base(1, "Trebuchet?!")
	{ }

	private ulong lineToNumberWithWords(string line)
	{
		KeyValuePair<string, string>[] numbers = {
			new KeyValuePair<string, string>("one", "1"),
			new KeyValuePair<string, string>("two", "2"),
			new KeyValuePair<string, string>("three", "3"),
			new KeyValuePair<string, string>("four", "4"),
			new KeyValuePair<string, string>("five", "5"),
			new KeyValuePair<string, string>("six", "6"),
			new KeyValuePair<string, string>("seven", "7"),
			new KeyValuePair<string, string>("eight", "8"),
			new KeyValuePair<string, string>("nine", "9"),
		};
		int i = 0;

		while (i < line.Length) {
			foreach (var pair in numbers) {
				if (i + pair.Key.Length > line.Length || line.Substring(i, pair.Key.Length) != pair.Key)
					continue;

				string tmpLine = "";

				tmpLine = line.Substring(0, i) + pair.Value;
				if (i + pair.Key.Length <= line.Length)
					tmpLine += line.Substring(i + pair.Key.Length);

				line = tmpLine;
				break;
			}
			if (line[i] >= '0' && line[i] <= '9')
				break;
			++i;
		}

		int j = line.Length - 1;
		while (j >= 0) {
			foreach (var pair in numbers) {
				if (j + pair.Key.Length > line.Length || line.Substring(j, pair.Key.Length) != pair.Key)
					continue;

				string tmpLine = "";

				tmpLine = line.Substring(0, j) + pair.Value;
				if (j + pair.Key.Length <= line.Length)
					tmpLine += line.Substring(j + pair.Key.Length);

				line = tmpLine;
				break;
			}
			if (line[j] >= '0' && line[j] <= '9')
				break;
			--j;
		}

		return (ulong)((line[i] - '0')*10 + (line[j] - '0'));
	}

	private ulong lineToNumber(string line)
	{
		int i = 0;
		int j = line.Length - 1;

		while(i < line.Length && (line[i] < '0' || line[i] > '9')) ++i;
		while(j >= 0 && (line[j] < '0' || line[j] > '9')) --j;

		return (ulong)((line[i] - '0')*10 + (line[j] - '0'));
	}

	override public ulong Part1(string[] lines)
	{
		ulong sumLines = 0;

		foreach( string line in lines )
			sumLines += lineToNumber(line);

		return sumLines;
	}

	override public ulong Part2(string[] lines)
	{
		ulong sumLines = 0;

		foreach( string line in lines )
			sumLines += lineToNumberWithWords(line);

		return sumLines;
	}
}
