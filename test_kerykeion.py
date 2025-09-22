
from kerykeion import AstrologicalSubject, KerykeionChartSVG

birth_chart = AstrologicalSubject("Kanye", 1977, 6, 8, 8, 45, "Atlanta", "US")
birth_chart_svg = KerykeionChartSVG(birth_chart)
birth_chart_svg.makeSVG()
print(dir(birth_chart_svg))
