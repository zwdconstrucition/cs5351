<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Flow Chart</title>

    <!-- 引入 Bootstrap 和图标库 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

    <style>
        body {
            background-color: #f8f9fa;
        }

        #canvas-container {
            max-width: 1200px;
            margin: 20px auto;
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            overflow: auto;
        }

        .export-btn {
            margin-top: 20px;
        }
    </style>

    <script src="../static/raphael.min.js"></script>
    <script src="../static/jquery-3.6.0.min.js"></script>
    <script src="../static/flowchart-latest.js"></script>
</head>

<body>
    <div class="container py-5">
        <div class="text-center mb-4">
            <h1 class="display-5 fw-bold">Modern Flowchart Generator</h1>
            <p class="text-muted">Create and export your flowchart with ease!</p>
        </div>

        <!-- Flowchart canvas -->
        <div id="canvas-container">
            <textarea id="code" style="display:none;">
                {{code}}
            </textarea>
            <div id="canvas"></div>
        </div>

        <!-- Export button -->
        <div class="text-center">
            <button id="export-btn" class="btn btn-primary export-btn">
                <i class="fas fa-download"></i> Export as PNG
            </button>
        </div>
    </div>

    <!-- 引入 Bootstrap 脚本 -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>

    <script>
        $(document).ready(function () {
            // 渲染流程图
            var code = $("#code").text();
            var chart = flowchart.parse(code);
            chart.drawSVG('canvas', {
                'line-width': 2,
                'maxWidth': 1000,
                'line-length': 8,
                'text-margin': 8,
                'font-size': 16,
                'font-family': 'Arial',
                'font-color': '#333',
                'line-color': '#666',
                'element-color': '#999',
                'fill': '#ffffff',
                'arrow-end': 'block',
                'scale': 0.8,
                'symbols': {
                    'start': { 'font-color': 'white', 'element-color': '#28a745', 'fill': '#28a745' },
                    'end': { 'class': 'end-element', 'font-color': 'white', 'fill': '#dc3545' }
                }
            });

            // 导出为 PNG
            $('#export-btn').click(function () {
                var svgElement = document.getElementById('canvas').querySelector('svg');
                var svgData = new XMLSerializer().serializeToString(svgElement);
                var canvas = document.createElement('canvas');
                var ctx = canvas.getContext('2d');
                var img = new Image();

                img.onload = function () {
                    canvas.width = img.width;
                    canvas.height = img.height;

                    // 绘制白色背景
                    ctx.fillStyle = 'white';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);

                    // 绘制 SVG 到 canvas
                    ctx.drawImage(img, 0, 0);

                    // 导出图片
                    var imgURI = canvas.toDataURL('image/png');
                    var link = document.createElement('a');
                    link.href = imgURI;
                    link.download = 'flowchart.png';
                    link.click();
                };
                img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgData);
            });
        });
    </script>
</body>

</html>
