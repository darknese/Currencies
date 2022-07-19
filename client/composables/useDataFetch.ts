import { useFetch, UseFetchOptions, useRuntimeConfig } from '#app';


export const useDataFetch = async (url: string | Request, options?: UseFetchOptions<unknown>) => {
  const { public: { API_URL } } = useRuntimeConfig()
  const apiUrl = API_URL + url
  return useFetch(apiUrl, options)
}
