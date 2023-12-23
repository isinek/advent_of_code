using AdventOfCode2023.Solvers;

namespace Tests
{
    public class TestDay6
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
			string[] test_input = {
				"Time:      7  15   30",
				"Distance:  9  40  200"
			};
			SolverDay6 solver = new SolverDay6();

			Assert.That(solver.Part1(test_input), Is.EqualTo(288));
        }

        [Test]
        public void Test2()
        {
			string[] test_input = {
				"Time:      7  15   30",
				"Distance:  9  40  200"
			};
			SolverDay6 solver = new SolverDay6();

			Assert.That(solver.Part2(test_input), Is.EqualTo(71503));
        }
    }
}
