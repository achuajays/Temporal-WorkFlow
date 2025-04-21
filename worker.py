import asyncio
import concurrent.futures
from temporalio.client import Client
from temporalio.worker import Worker

from activities import move_files
from workflows import FileTransferWorkflow, FileTransferWorkflow2to3


async def main():
    # Connect to Temporal server
    client = await Client.connect("localhost:7233")

    # Run the worker
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as activity_executor:
        worker = Worker(
            client,
            task_queue="file-transfer-queue",
            workflows=[FileTransferWorkflow, FileTransferWorkflow2to3],
            activities=[move_files],
            activity_executor=activity_executor,
        )
        await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
