export function shortDesc(inputString: string, chars: number): string {
  if (inputString.length > chars) {
    return inputString.substring(0, chars) + '...';
  } else {
    return inputString;
  }
}


export function stringToSlug(prevStr: string) {
  return prevStr
      .toLowerCase()                   // Convert to lowercase
      .replace(/[^\w\s-]/g, '')        // Remove special characters
      .trim()                          // Trim leading/trailing whitespace
      .replace(/\s+/g, '-')            // Replace spaces with hyphens
      .replace(/-+/g, '-');            // Replace multiple hyphens with a single hyphen
}
