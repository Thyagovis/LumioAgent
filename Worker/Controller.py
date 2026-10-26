from fastapi import APIRouter
from .Schemas import WorkerIn
from .AgentWorker import agent

router = APIRouter(prefix="/worker")

@router.post("/call")
async def call(workerIn : WorkerIn):

    result = await agent.run(workerIn.prompt)
    return result.output