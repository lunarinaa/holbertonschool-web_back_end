/* eslint-disable */
export default function getListStudentIds(objects) {
    let newArray = []
    newArray = objects.map((item) => item.id); 
    if (typeof objects !== Array) {
        return [];
    } else {
        return newArray;
    }
}