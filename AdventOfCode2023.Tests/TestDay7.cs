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
    }
}
