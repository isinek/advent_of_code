namespace AdventOfCode2023.Solvers;

public enum CamelCardsHandType {
	None,
	HighCard,
	OnePair,
	TwoPairs,
	ThreeOfKind,
	FullHouse,
	FourOfKind,
	FiveOfKind
};

public class CamelCardsHand : IComparable<CamelCardsHand>
{
	public static Dictionary<char, byte> CardValues = new Dictionary<char, byte> {
		{ 'A', 14 },
		{ 'K', 13 },
		{ 'Q', 12 },
		{ 'J', 11 },
		{ 'T', 10 },
		{ '9', 9 },
		{ '8', 8 },
		{ '7', 7 },
		{ '6', 6 },
		{ '5', 5 },
		{ '4', 4 },
		{ '3', 3 },
		{ '2', 2 },
		{ 'j', 1 }	/* Jocker */
	};

	public readonly CamelCardsHandType Type;
	public readonly string Cards;
	public readonly ulong Bid;

	private CamelCardsHandType findType()
	{
		uint[] cardPoints = new uint[15];

		foreach (char c in this.Cards)
			++cardPoints[CamelCardsHand.CardValues[c]];

		uint[] nCards = new uint[4]; 
		CamelCardsHandType type = CamelCardsHandType.HighCard;
		for(uint i = 2; i < 15; ++i) {
			if (cardPoints[i] == 5) {
				type = CamelCardsHandType.FiveOfKind;
				break;
			}
			else if (cardPoints[i] == 4) {
				type = CamelCardsHandType.FourOfKind;
				break;
			}
			++nCards[cardPoints[i]];
		}

		if (nCards[3] > 0)
			type = CamelCardsHandType.ThreeOfKind;
		if (nCards[2] > 0 && type == CamelCardsHandType.ThreeOfKind)
			type = CamelCardsHandType.FullHouse;
		else if (nCards[2] == 2)
			type = CamelCardsHandType.TwoPairs;
		else if (nCards[2] == 1)
			type = CamelCardsHandType.OnePair;

		switch(cardPoints[1]) {
			case 5:
			case 4:
				type = CamelCardsHandType.FiveOfKind;
				break;
			case 3:
				switch(type) {
					case CamelCardsHandType.OnePair:
						type = CamelCardsHandType.FiveOfKind;
						break;
					default:
						type = CamelCardsHandType.FourOfKind;
						break;
				}
				break;
			case 2:
				switch(type) {
					case CamelCardsHandType.ThreeOfKind:
						type = CamelCardsHandType.FiveOfKind;
						break;
					case CamelCardsHandType.OnePair:
						type = CamelCardsHandType.FourOfKind;
						break;
					default:
						type = CamelCardsHandType.ThreeOfKind;
						break;
				}
				break;
			case 1:
				switch(type) {
					case CamelCardsHandType.FourOfKind:
						type = CamelCardsHandType.FiveOfKind;
						break;
					case CamelCardsHandType.ThreeOfKind:
						type = CamelCardsHandType.FourOfKind;
						break;
					case CamelCardsHandType.TwoPairs:
						type = CamelCardsHandType.FullHouse;
						break;
					case CamelCardsHandType.OnePair:
						type = CamelCardsHandType.ThreeOfKind;
						break;
					default:
						type = CamelCardsHandType.OnePair;
						break;
				}
				break;
		}

		return type;
	}

	public CamelCardsHand(string cards, ulong bid)
	{
		this.Cards = cards;
		this.Bid = bid;
		this.Type = this.findType();
	}

	public static bool operator <(CamelCardsHand lhs, CamelCardsHand rhs)
	{
		if (lhs.Type == rhs.Type) {
			if (lhs.Cards == rhs.Cards)
				return false;

			for (int i = 0; i < lhs.Cards.Length; ++i) {
				if (lhs.Cards[i] == rhs.Cards[i])
					continue;

				return CamelCardsHand.CardValues[lhs.Cards[i]] < CamelCardsHand.CardValues[rhs.Cards[i]];
			}
		}

		return lhs.Type < rhs.Type;
	}

	public static bool operator >(CamelCardsHand lhs, CamelCardsHand rhs)
	{
		if (lhs.Type == rhs.Type) {
			if (lhs.Cards == rhs.Cards)
				return false;

			for (int i = 0; i < lhs.Cards.Length; ++i) {
				if (lhs.Cards[i] == rhs.Cards[i])
					continue;

				return CamelCardsHand.CardValues[lhs.Cards[i]] > CamelCardsHand.CardValues[rhs.Cards[i]];
			}
		}

		return lhs.Type > rhs.Type;
	}

	public int CompareTo(CamelCardsHand? other)
	{
		if (other == null)
			return 1;

		if (this < other)
			return -1;
		else if (this > other)
			return 1;
		return 0;
	}
}

public class SolverDay7 : SolverBase
{
	public SolverDay7()
		: base(7, "Camel Cards")
	{ }

    public override ulong Part1(string[] lines)
    {
		var hands = new List<CamelCardsHand>();

		foreach (string line in lines)
			hands.Add(new CamelCardsHand(line.Split()[0], ulong.Parse(line.Split()[1])));
		hands.Sort();

		ulong totalWinnings = 0;
		for (int i = 1; i <= hands.Count(); ++i)
			totalWinnings += ((ulong) i)*hands[i - 1].Bid;

        return totalWinnings;
    }

    public override ulong Part2(string[] lines)
    {
		var hands = new List<CamelCardsHand>();

		foreach (string line in lines)
			hands.Add(new CamelCardsHand(line.Split()[0].Replace("J", "j"), ulong.Parse(line.Split()[1])));
		hands.Sort();

		ulong totalWinnings = 0;
		for (int i = 1; i <= hands.Count(); ++i)
			totalWinnings += ((ulong) i)*hands[i - 1].Bid;

        return totalWinnings;
    }
}
