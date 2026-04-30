import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
from matplotlib.patches import Rectangle

# UTD location
lon, lat = - 96.75072866286929, 32.98683820680625

campus = gpd.GeoDataFrame(
    geometry=[Point(lon, lat)],
    crs="EPSG:4326"
).to_crs(epsg=3857)

# 2-mile radius
circle = gpd.GeoDataFrame(
    geometry=campus.buffer(8047),
    crs="EPSG:3857"
)

fig, ax = plt.subplots(figsize=(10, 10))

# map bounds
minx, miny, maxx, maxy = circle.total_bounds
padding = 300
ax.set_xlim(minx - padding, maxx + padding)
ax.set_ylim(miny - padding, maxy + padding)

# map
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Voyager, zoom=14)

# color 
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, color="#0f172a", alpha=0.2, zorder=2))

# radius
circle.plot(ax=ax, alpha=0.4, edgecolor="#38bdf8", linewidth=3, color="#38bdf8", zorder=3)

# campus point
campus.plot(ax=ax, markersize=160, color="#facc15", edgecolor="black", linewidth=2, zorder=4)

# campus label
ax.text(
    campus.geometry.x.iloc[0],
    campus.geometry.y.iloc[0] + 350,
    "UTD",
    fontsize=16,
    fontweight="bold",
    color="white",
    ha="center",
    zorder=5
)

#title
ax.set_title("Places Within 5 Miles of UTD", fontsize=24, fontweight="bold", color="white", pad=20)

fig.patch.set_facecolor("#0f172a")
ax.set_axis_off()
plt.tight_layout(pad=2)

highlight_circle = gpd.GeoDataFrame(
    geometry=[Point(-96.73406627506988, 32.9495555593101)],
    crs="EPSG:4326"
).to_crs(epsg=3857)

highlight_circle = gpd.GeoDataFrame(
    geometry=highlight_circle.buffer(1609),
    crs="EPSG:3857"
)

highlight_circle.plot(
    ax=ax,
    alpha=0.12,
    color="#fa15cc",
    edgecolor="#fa15cc",
    linewidth=3,
    zorder=5
)

highlight_circle_2 = gpd.GeoDataFrame(
    geometry=[Point(-96.74039860282575, 32.940443444665085)],
    crs="EPSG:4326"
).to_crs(epsg=3857)

highlight_circle_2 = gpd.GeoDataFrame(
    geometry=highlight_circle_2.buffer(1609),
    crs="EPSG:3857"
)

highlight_circle_2.plot(
    ax=ax,
    alpha=0.12,
    color="#fa1515",
    edgecolor="#fa1515",
    linewidth=3,
    zorder=5
)

# places
places = [
    {"name": "OMG Tacos", "lat": 32.94293694851955, "lon": -96.74319803462491, "shape": "circle", "color": "blue", "rating": 4, "label": "left"},
    {"name": "OG Chicken", "lat": 32.952038661932946, "lon": -96.72781425689165, "shape": "circle", "color": "blue", "rating": 4, "label": "top"},
    {"name": "Bora Bora", "lat": 32.97495864551868, "lon": -96.71411295923134, "shape": "circle", "color": "blue", "rating": 5, "label": "right"},
    {"name": "Velvet Taco", "lat": 32.97585386071342, "lon": -96.71737771382224, "shape": "circle", "color": "blue", "rating": 4, "label": "top"},
    {"name": "Junbi", "lat": 32.97622194776941, "lon": -96.72264872905316, "shape": "circle", "color": "blue", "rating": 5, "label": "bottom"},
    {"name": "Pax and Beneficia", "lat": 33.008181734889476, "lon": -96.71714085257634, "shape": "circle", "color": "blue", "rating": 5, "label": "top"},
    {"name": "7th Day Coffee", "lat": 32.940228639939455, "lon": -96.73602231645798, "shape": "circle", "color": "blue", "rating": 5, "label": "left"},
    {"name": "Torchys Tacos", "lat": 32.97625399866999, "lon": -96.72209788845961, "shape": "circle", "color": "blue", "rating": 4, "label": "left"},
    {"name": "Canes", "lat": 32.978658122294284, "lon": -96.76865638916519, "shape": "circle", "color": "blue", "rating": 5, "label": "top"},
    {"name": "Feng Cha", "lat": 32.99177272871219, "lon": -96.72787932902152, "shape": "circle", "color": "blue", "rating": 5, "label": "top"},
    {"name": "Chick-fil-A", "lat": 32.96133884221472, "lon": -96.77073096217347, "shape": "circle", "color": "blue", "rating": 5, "label": "left"},
    {"name": "Fat Straws", "lat": 32.97770804072288, "lon": -96.76230941906651, "shape": "circle", "color": "blue", "rating": 4, "label": "bottom"},
    {"name": "Sky Rocket", "lat": 32.99811162230038, "lon": -96.76894198811675, "shape": "circle", "color": "blue", "rating": 5, "label": "bottom"},
    {"name": "Medina", "lat": 32.94871302819809, "lon": -96.7312299983803, "shape": "circle", "color": "blue", "rating": 3, "label": "bottom"},
    {"name": "First Emperor Chinese Restaurant", "lat": 32.94960057528753, "lon": -96.73408773158921, "shape": "circle", "color": "blue", "rating": 4, "label": "left"},
    {"name": "Moriya Shokudo", "lat": 32.97733218519953, "lon": -96.76730059852501, "shape": "circle", "color": "blue", "rating": 5, "label": "left"},
    {"name": "Fukuro", "lat": 32.993427048731235, "lon": -96.7501837295768, "shape": "circle", "color": "blue", "rating": 3, "label": "top"},
    {"name": "McDonalds", "lat": 33.00085944660266, "lon": -96.76708058662895, "shape": "circle", "color": "blue", "rating": 5, "label": "top"},
    {"name": "Qdoba", "lat": 32.97719, "lon": -96.76691, "shape": "circle", "color": "blue", "rating": 3, "label": "top"},
    {"name": "AJ's Hot Chicken", "lat": 32.97531, "lon": -96.73548, "shape": "circle", "color": "blue", "rating": 4, "label": "right"},
    {"name": "Bawarchi", "lat": 32.97589, "lon": -96.72078, "shape": "circle", "color": "blue", "rating": 4, "label": "left"},
    {"name": "Taco Bell", "lat": 32.96377, "lon": -96.73375, "shape": "circle", "color": "blue", "rating": 5, "label": "left"},
    {"name": "La La Land", "lat": 32.97595, "lon": -96.73015, "shape": "circle", "color": "blue", "rating": 4, "label": "top"},
    {"name": "Panda Express", "lat": 32.97758, "lon": -96.76389, "shape": "circle", "color": "blue", "rating": 4, "label": "right"},
    {"name": "Masala Wok", "lat": 32.97744, "lon": -96.76184, "shape": "circle", "color": "blue", "rating": 3, "label": "left"},
    {"name": "Insomnia", "lat": 32.9940610405489, "lon": -96.74959673553462, "shape": "circle", "color": "blue", "rating": 4, "label": "right"},
    {"name": "Pei Wei", "lat": 32.97724, "lon": -96.75972, "shape": "circle", "color": "blue", "rating": 2, "label": "bottom"},
    {"name": "Bagel Cafe 21", "lat": 32.99849, "lon": -96.7685, "shape": "circle", "color": "blue", "rating": 4, "label": "left"},
    {"name": "Chilis", "lat": 32.94014, "lon": -96.73556, "shape": "circle", "color": "blue", "rating": 3, "label": "bottom"},
    {"name": "Pizza Hut", "lat": 32.97535, "lon": -96.73551, "shape": "circle", "color": "blue", "rating": 4, "label": "top"},
    {"name": "Tikka n Kabab", "lat": 32.98557, "lon": -96.77072, "shape": "circle", "color": "blue", "rating": 3, "label": "left"},
    {"name": "Dominos", "lat": 32.96362, "lon": -96.73363, "shape": "circle", "color": "blue", "rating": 5, "label": "right"},
]



for p in places:
    point = gpd.GeoSeries([Point(p["lon"], p["lat"])], crs="EPSG:4326").to_crs(epsg=3857)
    x = point.geometry.x.iloc[0]
    y = point.geometry.y.iloc[0]

    marker = "o"
    color = "#3b82f6"

    ax.scatter(
        x,
        y,
        s=160,
        marker=marker,
        color=color,
        edgecolor="white",
        linewidth=1.5,
        zorder=6
    )
    #orientation of text
    if p["label"] == "top":
        dx, dy, ha, va = 0, 320, "center", "bottom"
    elif p["label"] == "bottom":
        dx, dy, ha, va = 0, -600, "center", "top"
    elif p["label"] == "left":
        dx, dy, ha, va = -350, 0, "right", "center"
    elif p["label"] == "right":
        dx, dy, ha, va = 350, 0, "left", "center"

    stars = "★" * p["rating"]

    ax.text(
        x + dx,
        y + dy + 320,
        stars,
        fontsize=10,
        color="#facc15",
        ha=ha,
        va=va,
        fontweight="bold",
        zorder=7
    )

    ax.text(
        x + dx,
        y + dy,
        p["name"],
        fontsize=10,
        color="white",
        ha=ha,
        va=va,
        fontweight="bold",
        zorder=7
    )

plt.show()