## 基础知识
在绘图结构中，figure创建窗口，subplot创建子图。
所有的绘画只能在子图上进行。
plt表示当前子图，若没有就创建一个子图。

Figure：面板(图)，matplotlib中的所有图像都是位于figure对象中，一个图像只能有一个figure对象。
Subplot：子图，figure对象下创建一个或多个subplot对象(即axes)用于绘制图像。

### 参数
axex: 设置坐标轴边界和表面的颜色、坐标刻度值大小和网格的显示
figure: 控制dpi、边界颜色、图形大小、和子区( subplot)设置
font: 字体集（font family）、字体大小和样式设置
grid: 设置网格颜色和线性
legend: 设置图例和其中的文本的显示
line: 设置线条（颜色、线型、宽度等）和标记
patch: 是填充2D空间的图形对象，如多边形和圆。控制线宽、颜色和抗锯齿设置等。
savefig: 可以对保存的图形进行单独设置。例如，设置渲染的文件的背景为白色。
verbose: 设置matplotlib在执行期间信息输出，如silent、helpful、debug和debug-annoying。
xticks和yticks: 为x,y轴的主刻度和次刻度设置颜色、大小、方向，以及标签大小。

### 