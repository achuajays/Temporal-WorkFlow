import asyncio
from datetime import timedelta
from temporalio.client import Client, Schedule, ScheduleActionStartWorkflow, ScheduleSpec, ScheduleIntervalSpec
from workflows import FileTransferWorkflow, FileTransferWorkflow2to3


async def main():
    client = await Client.connect("localhost:7233")

    # Schedule for 1 -> 2
    await client.create_schedule(
        "file-transfer-schedule-1-to-2",
        Schedule(
            action=ScheduleActionStartWorkflow(
                FileTransferWorkflow.run,
                args=["1", "2"],
                id="file-transfer-workflow-1-to-2",
                task_queue="file-transfer-queue",
            ),
            spec=ScheduleSpec(
                intervals=[ScheduleIntervalSpec(every=timedelta(minutes=1))]
            )
        )
    )

    print("Scheduled workflow: folder 1 -> 2")

    # Schedule for 2 -> 3
    await client.create_schedule(
        "file-transfer-schedule-2-to-3",
        Schedule(
            action=ScheduleActionStartWorkflow(
                FileTransferWorkflow2to3.run,
                args=["2", "3"],
                id="file-transfer-workflow-2-to-3",
                task_queue="file-transfer-queue",
            ),
            spec=ScheduleSpec(
                intervals=[ScheduleIntervalSpec(every=timedelta(minutes=1))]
            )
        )
    )

    print("Scheduled workflow: folder 2 -> 3")


if __name__ == "__main__":
    asyncio.run(main())
