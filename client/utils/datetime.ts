// Array of month names for formatting
const monthNames: string[] = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December',
];

export function formatReadableDate(inputDate: string): string {
  const dateObject: Date = new Date(inputDate);

  // Get month, day, and year from the date object
  const month: string = monthNames[dateObject.getMonth()];
  const day: number = dateObject.getDate();
  const year: number = dateObject.getFullYear();

  // Formatted date string in the desired format
  const formattedDate: string = `${month} ${day}, ${year}`;

  return formattedDate;
}

export function formatRelativeDate(inputDate: string): string {
  const dateObject: Date = new Date(inputDate);
  const currentDate: Date = new Date();

  // Calculate the difference in milliseconds between the current date and input date
  const diffMillis: number = currentDate.getTime() - dateObject.getTime();
  const diffMinutes: number = Math.round(diffMillis / (1000 * 60));

  if (diffMinutes < 60) {
    // Show relative time if less than an hour ago
    return `Last updated ${diffMinutes} mins ago`;
  } else {
    // Show formatted date if not today
    return formatReadableDate(inputDate);
  }
}
