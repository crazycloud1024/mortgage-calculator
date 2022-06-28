from app.core.server import create_app

app = create_app()

if __name__ == "__main__":

    import uvicorn

    for route in app.routes:
        if hasattr(route, "methods"):
            print({'path': route.path, 'name': route.name, 'methods': route.methods})

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
