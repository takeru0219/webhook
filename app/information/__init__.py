from fastapi import APIRouter, status
from fastapi.responses import Response

from app.information.melon import get_melon
from app.slack import post

router = APIRouter(prefix='/info')


@router.get('/melon')
def get_melon_ranking():
    songs = get_melon()
    post('\n'.join(
        [f'{i}. {song.title} - {song.artist}' for i, song in enumerate(songs)]), 'Melon')

    return Response(status_code=status.HTTP_200_OK)
