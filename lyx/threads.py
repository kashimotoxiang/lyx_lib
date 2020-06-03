import multiprocessing


def map(func, data, cpu=(multiprocessing.cpu_count() - 1)):
    with multiprocessing.Pool(cpu) as pool:
        result = pool.map(func, data)
        return result


def async_map(func, data, cpu=(multiprocessing.cpu_count() - 1)):
    with multiprocessing.Pool(processes=cpu) as pool:
        async_result = pool.map_async(func, data)
        pool.close()
        pool.join()
        results = async_result.get()
        return results
