import { createContext, useCallback, useContext, useEffect, useMemo, useState } from "react";

const CartContext = createContext(null);
const STORAGE_KEY = "neon-pulse-cart";

function readCart() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
  } catch {
    return [];
  }
}

export function CartProvider({ children }) {
  const [items, setItems] = useState(readCart);
  const [open, setOpen] = useState(false);
  const [toast, setToast] = useState(null);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    } catch {
      return;
    }
  }, [items]);

  useEffect(() => {
    if (!toast) return undefined;
    const timer = setTimeout(() => setToast(null), 2600);
    return () => clearTimeout(timer);
  }, [toast]);

  const add = useCallback((product) => {
    setItems((current) => {
      const found = current.find((item) => item.id === product.id);
      if (found) return current.map((item) => (item.id === product.id ? { ...item, qty: item.qty + 1 } : item));
      const { id, name, price, image, url, brand } = product;
      return [...current, { id, name, price, image, url, brand, qty: 1 }];
    });
    setToast({ text: `${product.name} added to cart`, id: Date.now() });
  }, []);

  const update = useCallback((id, qty) => {
    setItems((current) => (qty <= 0 ? current.filter((item) => item.id !== id) : current.map((item) => (item.id === id ? { ...item, qty } : item))));
  }, []);

  const clear = useCallback(() => setItems([]), []);

  const value = useMemo(() => {
    const count = items.reduce((sum, item) => sum + item.qty, 0);
    const total = items.reduce((sum, item) => sum + item.qty * item.price, 0);
    return { items, count, total, add, update, clear, open, setOpen, toast, setToast };
  }, [items, add, update, clear, open, toast]);

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
}

export function useCart() {
  return useContext(CartContext);
}
