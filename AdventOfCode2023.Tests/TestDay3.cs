using AdventOfCode2023.Solvers;

namespace Tests
{
    public class TestDay3
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
			string[] test_input = {
				"467..114..",
				"...*......",
				"..35..633.",
				"......#...",
				"617*......",
				".....+.58.",
				"..592.....",
				"......755.",
				"...$.*....",
				".664.598.."
			};
			SolverDay3 solver = new SolverDay3();

			Assert.That(solver.Part1(test_input), Is.EqualTo(4361));
		}

        [Test]
        public void Test2()
        {
			string[] test_input = {
				"467..114..",
				"...*......",
				"..35..633.",
				"......#...",
				"617*......",
				".....+.58.",
				"..592.....",
				"......755.",
				"...$.*....",
				".664.598.."
			};
			SolverDay3 solver = new SolverDay3();

			Assert.That(solver.Part2(test_input), Is.EqualTo(467835));
		}
    }
}
