//fetch habit information from api here and pass it into the proper components using getStaticProps or getServerSideProps()
//need to plan a mock design or something simple to begin diving in

function getHabitsList<T>(url: string): Promise<T> {
    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(response.statusText)
            }
            return response.json() as Promise<T>
        })
}

export async function getHabitsData<T>(): json {
    const habits = await getHabitsList("http://127.0.0.1:8000/habits")
    return habits
}