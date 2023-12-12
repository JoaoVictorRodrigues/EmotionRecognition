import asyncio
from FaceStudy import AsyncFaceStudy, SyncFaceStudy

# Função de teste para a versão assíncrona com callback
async def test_async_with_callback():
    async_face_study = AsyncFaceStudy(analyze_type='age', window='Async With Callback')
    await async_face_study.run()

# Função de teste para a versão assíncrona sem callback
async def test_async_without_callback():
    async_face_study = AsyncFaceStudy(analyze_type='age', window='Async Without Callback')
    await async_face_study.run()

# Função de teste para a versão síncrona
def test_sync():
    sync_face_study = SyncFaceStudy(analyze_type='age', window='Sync Face Study')
    sync_face_study.run()

# Executar os testes
asyncio.run(test_async_with_callback())
asyncio.run(test_async_without_callback())
test_sync()
