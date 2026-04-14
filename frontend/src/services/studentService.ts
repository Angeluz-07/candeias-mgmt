import api from "@/api/client";

export const StudentService = {
  getStudents: () => api.get("/students"),
};
