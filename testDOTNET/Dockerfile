# Stage 1
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build

WORKDIR /src

COPY ["src/TestDotnet/TestDotnet.csproj", "TestDotnet/"]
RUN dotnet restore "TestDotnet/TestDotnet.csproj"

COPY ["src/TestDotnet", "TestDotnet/"]
WORKDIR /src/TestDotnet
RUN dotnet build "TestDotnet/TestDotnet.csproj" -c Release -o /app/build

# Stage 2
FROM build AS publish
RUN dotnet publish "TestDotnet.csproj" -c Release -o /app/publish

# Stage 3
FROM mcr.microsoft.com/dotnet/aspnet:9.0
ENV ASPNETCORE_HTTP_PORTS=5000
EXPOSE 5000
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "TestDotnet.dll"]
