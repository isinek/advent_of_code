using AdventOfCode2023.Solvers;

namespace Tests
{
    public class TestDay9
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
			string[] test_input = {
				"0 3 6 9 12 15",
				"1 3 6 10 15 21",
				"10 13 16 21 30 45"
			};
			SolverDay9 solver = new SolverDay9();

			Assert.That(solver.Part1(test_input), Is.EqualTo(114));
        }

        [Test]
        public void Test2()
        {
			string[] test_input = {
				"0 3 6 9 12 15",
				"1 3 6 10 15 21",
				"10 13 16 21 30 45"
			};
			SolverDay9 solver = new SolverDay9();

			Assert.That(solver.Part2(test_input), Is.EqualTo(2));
        }
    }
}
