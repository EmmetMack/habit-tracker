//fetch habit information from api here and pass it into the proper components using getStaticProps or getServerSideProps()
//need to plan a mock design or something simple to begin diving in

async function getHabitsList<T>(url: string): Promise<T> {
    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(response.statusText)
            }
            return response.json() as Promise<T>
        })
}

async function createHabitCall<T>(url: string, data: json): Promise<T> {
    return fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify(data),
    }).then(response => {
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

export async function createHabit<T>(data: json): json {
    const habit = await createHabitCall("http://127.0.0.1:8000/habits", data);
    return habit
}
  



