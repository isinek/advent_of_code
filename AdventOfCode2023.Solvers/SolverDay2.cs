namespace AdventOfCode2023.Solvers;

public class SolverDay2 : SolverBase
{
	public SolverDay2()
		: base(2, "Cube Conundrum")
	{ }

	private uint GameValidator(uint redLimit, uint greenLimit, uint blueLimit, string line)
	{
		uint gameId = UInt32.Parse(line.Substring(5).Split(":")[0]);
		string[] games = line.Split(": ")[1].Split("; ");

		foreach (string game in games) {
			string[] cubes = game.Split(", ");

			foreach (string cubeType in cubes) {
				uint nCubes = UInt32.Parse(cubeType.Split(" ")[0]);
				string color = cubeType.Split(" ")[1];

				switch(color[0]) {
					case 'r':
						if (nCubes > redLimit)
							return 0;
						break;
					case 'g':
						if (nCubes > greenLimit)
							return 0;
						break;
					case 'b':
						if (nCubes > blueLimit)
							return 0;
						break;
				}
			}
		}

		return gameId;
	}

	private uint GamePower(string line)
	{
		string[] games = line.Split(": ")[1].Split("; ");
		uint[] minimalRequiredCubes = { 0, 0, 0 };

		foreach (string game in games) {
			string[] cubes = game.Split(", ");

			foreach (string cubeType in cubes) {
				uint nCubes = UInt32.Parse(cubeType.Split(" ")[0]);
				string color = cubeType.Split(" ")[1];

				switch(color[0]) {
					case 'r':
						if (nCubes > minimalRequiredCubes[0])
							minimalRequiredCubes[0] = nCubes;
						break;
					case 'g':
						if (nCubes > minimalRequiredCubes[1])
							minimalRequiredCubes[1] = nCubes;
						break;
					case 'b':
						if (nCubes > minimalRequiredCubes[2])
							minimalRequiredCubes[2] = nCubes;
						break;
				}
			}
		}

		return minimalRequiredCubes[0]*minimalRequiredCubes[1]*minimalRequiredCubes[2];
	}

	override public ulong Part1(string[] lines)
	{
		ulong gameIdSum = 0;

		foreach (string line in lines)
			gameIdSum += GameValidator(12, 13, 14, line);

		return gameIdSum;
	}

	override public ulong Part2(string[] lines)
	{
		ulong gamePowerSum = 0;

		foreach (string line in lines)
			gamePowerSum += GamePower(line);

		return gamePowerSum;
	}
}
