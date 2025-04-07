FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

WORKDIR /src
COPY [ "./AdventOfCode2023.sln", "./" ]
COPY [ "./AdventOfCode2023.Console/AdventOfCode2023.Console.csproj", "./AdventOfCode2023.Console/" ]
COPY [ "./AdventOfCode2023.Solvers/AdventOfCode2023.Solvers.csproj", "./AdventOfCode2023.Solvers/" ]
COPY [ "./AdventOfCode2023.Tests/AdventOfCode2023.Tests.csproj", "./AdventOfCode2023.Tests/" ]
RUN [ "dotnet", "restore" ]

COPY [ "./AdventOfCode2023.Console/.", "./AdventOfCode2023.Console/" ]
COPY [ "./AdventOfCode2023.Solvers/.", "./AdventOfCode2023.Solvers/" ]
COPY [ "./AdventOfCode2023.Tests/.", "./AdventOfCode2023.Tests/" ]

RUN [ "dotnet", "build", "./AdventOfCode2023.Solvers/", "-c", "Release", "-o", "/app/build/" ]
RUN [ "dotnet", "build", "./AdventOfCode2023.Console/", "-c", "Release", "-o", "/app/build/" ]

RUN [ "dotnet", "test", "--no-build" ]

RUN [ "dotnet", "publish", "./AdventOfCode2023.Console/", "-c", "Release", "-o", "/app/publish/" ]

FROM mcr.microsoft.com/dotnet/sdk:8.0
WORKDIR /resources
COPY [ "./resources/.", "./" ]

WORKDIR /app
COPY --from=build /app/publish/ ./
ENTRYPOINT [ "dotnet", "AdventOfCode2023.Console.dll" ]
