export default function Avatar({ member, size = 96 }) {
  const [from, to] = member.gradient;
  return (
    <span className="avatar" style={{ width: size, height: size, fontSize: size * 0.34, background: `linear-gradient(135deg, ${from}, ${to})` }}>
      {member.initials}
    </span>
  );
}
