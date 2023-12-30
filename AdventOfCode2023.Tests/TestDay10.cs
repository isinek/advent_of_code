using AdventOfCode2023.Solvers;

namespace Tests
{
    public class TestDay10
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
			string[] test_input = {
				"-L|F7",
				"7S-7|",
				"L|7||",
				"-L-J|",
				"L|-JF"
			};
			SolverDay10 solver = new SolverDay10();

			Assert.That(solver.Part1(test_input), Is.EqualTo(4));
        }

        [Test]
        public void Test2()
        {
			string[] test_input = {
				"7-F7-",
				".FJ|7",
				"SJLL7",
				"|F--J",
				"LJ.LJ"
			};
			SolverDay10 solver = new SolverDay10();

			Assert.That(solver.Part1(test_input), Is.EqualTo(8));
        }

        [Test]
        public void Test3()
        {
			string[] test_input = {
				"...........",
				".S-------7.",
				".|F-----7|.",
				".||.....||.",
				".||.....||.",
				".|L-7.F-J|.",
				".|..|.|..|.",
				".L--J.L--J.",
				"..........."
			};
			SolverDay10 solver = new SolverDay10();

			Assert.That(solver.Part2(test_input), Is.EqualTo(4));
        }

        [Test]
        public void Test4()
        {
			string[] test_input = {
				"..........",
				".S------7.",
				".|F----7|.",
				".||....||.",
				".||....||.",
				".|L-7F-J|.",
				".|..||..|.",
				".L--JL--J.",
				".........."
			};
			SolverDay10 solver = new SolverDay10();

			Assert.That(solver.Part2(test_input), Is.EqualTo(4));
        }

        [Test]
        public void Test5()
        {
			string[] test_input = {
				".F----7F7F7F7F-7....",
				".|F--7||||||||FJ....",
				".||.FJ||||||||L7....",
				"FJL7L7LJLJ||LJ.L-7..",
				"L--J.L7...LJS7F-7L7.",
				"....F-J..F7FJ|L7L7L7",
				"....L7.F7||L7|.L7L7|",
				".....|FJLJ|FJ|F7|.LJ",
				"....FJL-7.||.||||...",
				"....L---J.LJ.LJLJ..."
			};
			SolverDay10 solver = new SolverDay10();

			Assert.That(solver.Part2(test_input), Is.EqualTo(8));
        }

        [Test]
        public void Test6()
        {
			string[] test_input = {
				"FF7FSF7F7F7F7F7F---7",
				"L|LJ||||||||||||F--J",
				"FL-7LJLJ||||||LJL-77",
				"F--JF--7||LJLJ7F7FJ-",
				"L---JF-JLJ.||-FJLJJ7",
				"|F|F-JF---7F7-L7L|7|",
				"|FFJF7L7F-JF7|JL---7",
				"7-L-JL7||F7|L7F-7F7|",
				"L.L7LFJ|||||FJL7||LJ",
				"L7JLJL-JLJLJL--JLJ.L"
			};
			SolverDay10 solver = new SolverDay10();

			Assert.That(solver.Part2(test_input), Is.EqualTo(10));
        }
    }
}
