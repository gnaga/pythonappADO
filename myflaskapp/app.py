"""Main Flask application module."""

from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Flask App</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: #333;
        }
        .container {
            background: white;
            border-radius: 12px;
            padding: 40px 50px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            text-align: center;
            max-width: 500px;
        }
        h1 {
            color: #667eea;
            margin-bottom: 10px;
        }
        p {
            color: #666;
            line-height: 1.6;
        }
        .status {
            display: inline-block;
            background: #d4edda;
            color: #155724;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: bold;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>My Flask Application</h1>
        <p>Jfrog Sample Flask application deployed via Azure DevOps pipeline, packaged as a Python wheel and running inside a Docker container.</p>
        <div class="status">Running</div>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    """Render the home page."""
    return render_template_string(HTML_TEMPLATE)


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "application": "myflaskapp", "version": "1.0.0"})


def main():
    """Entry point for the application."""
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
