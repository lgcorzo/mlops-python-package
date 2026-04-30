import asyncio
import time
import threading


def sync_prediction():
    """Simulates a CPU-bound synchronous prediction call."""
    print("  [Sync] Starting prediction...")
    time.sleep(2)  # Simulate 2 seconds of blocking work
    print("  [Sync] Prediction complete.")
    return {"result": "success"}


async def async_health_check():
    """Simulates an asynchronous health check that should remain responsive."""
    for i in range(5):
        print(f"  [Async] Health check {i + 1}...")
        await asyncio.sleep(0.5)


async def run_blocking_scenario():
    print("\nScenario: Blocking Sync Call in Event Loop")
    print("-" * 40)
    start_time = time.time()

    # In a real FastAPI app, calling sync_prediction() directly in an async def endpoint
    # would block the entire event loop.

    health_task = asyncio.create_task(async_health_check())

    print("Calling sync_prediction() directly...")
    sync_prediction()

    await health_task

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f}s")
    print("Note: Notice how health checks were delayed until prediction finished.")


async def run_non_blocking_scenario():
    print("\nScenario: Non-Blocking Call using ThreadPool")
    print("-" * 40)

    # We'll use asyncio.to_thread which is similar to what run_in_threadpool does
    # (available in Python 3.9+)

    start_time = time.time()

    health_task = asyncio.create_task(async_health_check())

    print("Calling sync_prediction() in a thread...")
    prediction_task = asyncio.to_thread(sync_prediction)

    await asyncio.gather(health_task, prediction_task)

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f}s")
    print("Note: Notice how health checks ran concurrently with prediction.")


if __name__ == "__main__":
    asyncio.run(run_blocking_scenario())
    asyncio.run(run_non_blocking_scenario())
