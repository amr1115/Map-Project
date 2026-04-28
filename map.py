import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
from matplotlib.patches import Rectangle

# UTD location
lon, lat = -96.7501, 32.9858

campus = gpd.GeoDataFrame(
    geometry=[Point(lon, lat)],
    crs="EPSG:4326"
).to_crs(epsg=3857)

# 2-mile radius
circle = gpd.GeoDataFrame(
    geometry=campus.buffer(3219),
    crs="EPSG:3857"
)

fig, ax = plt.subplots(figsize=(10, 10))

# set map bounds first
minx, miny, maxx, maxy = circle.total_bounds
padding = 300
ax.set_xlim(minx - padding, maxx + padding)
ax.set_ylim(miny - padding, maxy + padding)

# base map
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Voyager, zoom=14)

# dark overlay
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

ax.set_title("Places Within 2 Miles of UTD", fontsize=24, fontweight="bold", color="white", pad=20)

fig.patch.set_facecolor("#0f172a")
ax.set_axis_off()
plt.tight_layout(pad=2)

plt.show()