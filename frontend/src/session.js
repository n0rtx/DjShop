import { createContext, useContext } from "react";

export const SessionContext = createContext({ user: null, csrf: "", go: () => {} });

export function useSession() {
  return useContext(SessionContext);
}
