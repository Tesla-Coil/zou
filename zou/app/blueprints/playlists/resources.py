from flask_restful import Resource
from flask_jwt_extended import jwt_required

from zou.app.services import playlists_service, user_service


class ProjectPlaylistsResource(Resource):

    @jwt_required
    def get(self, project_id):
        user_service.check_project_access(project_id)
        return playlists_service.all_playlists_for_project(project_id), 200
