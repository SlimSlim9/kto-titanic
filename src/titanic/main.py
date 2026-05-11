import uvicorn
from titanic.api.infer import app

def main():
    # Démarre le serveur sur le port 8080
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()