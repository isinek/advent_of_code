namespace AdventOfCode2023.Solvers;

public class SolverDay4 : SolverBase
{
	public SolverDay4()
		: base(4, "Scratchcards")
	{}

	private int cardScore(uint[] winningNumbers, uint[] cardNumbers)
	{
		int score = 0;

		foreach (uint winningNumber in winningNumbers)
			if (cardNumbers.Contains(winningNumber))
				++score;

		return score;
	}

    public override ulong Part1(string[] lines)
    {
		ulong sumPoints = 0;

		foreach (string line in lines) {
			string[] numbers = line.Split(": ")[1].Trim().Split(" | ");
			uint[] winningNumbers = numbers[0]
							.Split()
							.Where(x => x.Length > 0)
							.Select(x => uint.Parse(x.Trim()))
							.ToArray();
			uint[] cardNumbers = numbers[1]
							.Split()
							.Where(x => x.Length > 0)
							.Select(x => uint.Parse(x.Trim()))
							.ToArray();

			sumPoints += (((ulong) 1) << cardScore(winningNumbers, cardNumbers))/2;
		}

		return sumPoints;
    }

    public override ulong Part2(string[] lines)
    {
		ulong sumCards = 0;
		var cardPoints = new List<int>();
		var q = new Queue<int>();

		foreach (string line in lines) {
			string[] numbers = line.Split(": ")[1].Trim().Split(" | ");
			uint[] winningNumbers = numbers[0]
							.Split()
							.Where(x => x.Length > 0)
							.Select(x => uint.Parse(x.Trim()))
							.ToArray();
			uint[] cardNumbers = numbers[1]
							.Split()
							.Where(x => x.Length > 0)
							.Select(x => uint.Parse(x.Trim()))
							.ToArray();

			q.Enqueue(cardPoints.Count);
			cardPoints.Add(cardScore(winningNumbers, cardNumbers));
		}

		while(q.Any()) {
			int card = q.Dequeue();

			for (int i = 1; i <= cardPoints[card]; ++i)
				q.Enqueue(card + i);

			++sumCards;
		}

		return sumCards;
    }
}
