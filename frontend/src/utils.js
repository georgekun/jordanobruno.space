import axios from 'axios'

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

export function download(url) {
    axios.get(url, {
        responseType: 'blob' // Устанавливаем тип ответа как blob
    })
        .then(response => {
            const disposition = response.headers['content-disposition'];
            const matches = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/.exec(disposition);
            let filename = matches && matches[1] ? matches[1].replace(/['"]/g, '') : 'download'; // Получаем имя файла из заголовка

            if (decodeURIComponent(filename) !== filename) {
                filename = decodeURIComponent(filename);
            }
            
            const blob = new Blob([response.data]); // Создаем Blob из полученных данных
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', filename); // Устанавливаем имя файла для скачивания
            document.body.appendChild(link);
            link.click();
            link.parentNode.removeChild(link);
        })
        .catch(error => {
            console.error('Ошибка загрузки файла:', error);
        });
}