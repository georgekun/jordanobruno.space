export function createNewFormData(obj, exlude) {

    let data = new FormData()
    const keys = Object.keys(obj)
    for (const key of keys) {
        if (exlude.indexOf(key) === -1) {
            data.append(key, obj[key])
        }
    }

    return data
}