from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .oqs_wrapper import generate_dilithium_keypair

app = FastAPI()

class KeyPairResponse(BaseModel):
    public_key: str
    private_key: str

@app.get("/generate-keypair", response_model=KeyPairResponse)
async def generate_keypair():
    try:
        public_key, private_key = generate_dilithium_keypair()
        return {"public_key": public_key, "private_key": private_key}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)