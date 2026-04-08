export const StudentService = {
    async getStudents(params: any) {
        // En un enfoque profesional, aquí usarías axios.get con los params
        // params contiene: page, rows, sortField, sortOrder, filters
        const queryParams = new URLSearchParams({
            page: (params.page + 1).toString(), // PrimeVue es 0-indexed
            limit: params.rows.toString(),
            sort: params.sortField || '',
            order: params.sortOrder === 1 ? 'asc' : 'desc'
        }).toString();

        const response = await fetch(`http://localhost:8000/students`);
        return await response.json(); // Debe retornar { data: [], totalRecords: 100 }
    }
};