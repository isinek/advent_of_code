using AdventOfCode2023.Solvers;

namespace Tests
{
    public class TestDay7
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
			string[] test_input = {
				"32T3K 765",
				"T55J5 684",
				"KK677 28",
				"KTJJT 220",
				"QQQJA 483"
			};
			SolverDay7 solver = new SolverDay7();

			Assert.That(solver.Part1(test_input), Is.EqualTo(6440));
        }

        [Test]
        public void Test2()
        {
			string[] test_input = {
				"32T3K 765",
				"T55J5 684",
				"KK677 28",
				"KTJJT 220",
				"QQQJA 483"
			};
			SolverDay7 solver = new SolverDay7();

			Assert.That(solver.Part2(test_input), Is.EqualTo(5905));
        }

        [Test]
        public void CamelCardsHandTypeCheck()
        {
			KeyValuePair<string, CamelCardsHandType>[] test_inputs = {
				new KeyValuePair<string, CamelCardsHandType>("23456", CamelCardsHandType.HighCard),
				new KeyValuePair<string, CamelCardsHandType>("j2345", CamelCardsHandType.OnePair),
				new KeyValuePair<string, CamelCardsHandType>("j2234", CamelCardsHandType.ThreeOfKind),
				new KeyValuePair<string, CamelCardsHandType>("j2233", CamelCardsHandType.FullHouse),
				new KeyValuePair<string, CamelCardsHandType>("j2223", CamelCardsHandType.FourOfKind),
				new KeyValuePair<string, CamelCardsHandType>("j2222", CamelCardsHandType.FiveOfKind),
				new KeyValuePair<string, CamelCardsHandType>("jj234", CamelCardsHandType.ThreeOfKind),
				new KeyValuePair<string, CamelCardsHandType>("jj224", CamelCardsHandType.FourOfKind),
				new KeyValuePair<string, CamelCardsHandType>("jj222", CamelCardsHandType.FiveOfKind),
				new KeyValuePair<string, CamelCardsHandType>("jjj23", CamelCardsHandType.FourOfKind),
				new KeyValuePair<string, CamelCardsHandType>("jjj22", CamelCardsHandType.FiveOfKind),
				new KeyValuePair<string, CamelCardsHandType>("jjjj2", CamelCardsHandType.FiveOfKind),
				new KeyValuePair<string, CamelCardsHandType>("jjjjj", CamelCardsHandType.FiveOfKind)
			};

			foreach (var test in test_inputs) {
				CamelCardsHand hand = new CamelCardsHand(test.Key, 0);
				Assert.That(hand.Type, Is.EqualTo(test.Value));
			}
        }
    }
}
