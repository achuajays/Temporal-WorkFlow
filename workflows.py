from datetime import timedelta
import asyncio
from temporalio import workflow

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from activities import move_files


@workflow.defn
class FileTransferWorkflow:
    @workflow.run
    async def run(self, source_folder: str, destination_folder: str) -> None:
        while True:
            result = await workflow.execute_activity(
                move_files,
                args=(source_folder, destination_folder),
                schedule_to_close_timeout=timedelta(minutes=1)
            )

            workflow.logger.info(f"Activity result: {result}")

            await asyncio.sleep(60)
            await workflow.continue_as_new(args=(source_folder, destination_folder))


@workflow.defn
class FileTransferWorkflow2to3:
    @workflow.run
    async def run(self, source_folder: str, destination_folder: str) -> None:
        while True:
            result = await workflow.execute_activity(
                move_files,
                args=(source_folder, destination_folder),
                schedule_to_close_timeout=timedelta(minutes=1)
            )

            workflow.logger.info(f"[2->3] Activity result: {result}")

            await asyncio.sleep(60)
            await workflow.continue_as_new(args=(source_folder, destination_folder))
